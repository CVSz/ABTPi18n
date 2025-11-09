"""// ZeaZDev [Backend Trading Bot Runner Core] //
// Project: Auto Bot Trader i18n //
// Version: 1.0.0 (Omega Scaffolding) //
// Author: ZeaZDev Meta-Intelligence (Generated) //
// --- DO NOT EDIT HEADER --- //"""
import asyncio
import time
from typing import Dict, Any
from prisma import Prisma
from src.trading.strategy_interface import StrategyRegistry
from src.services.exchange_service import ExchangeConnector
from tenacity import retry, stop_after_attempt, wait_fixed

class RiskManager:
    def __init__(self, max_drawdown: float = 0.25, max_position_fraction: float = 0.1):
        self.max_drawdown = max_drawdown
        self.max_position_fraction = max_position_fraction

    async def assess(self, context: Dict[str, Any], signal_payload: Dict[str, Any]) -> bool:
        # Simplified risk: always allow if signal != HOLD
        if signal_payload.get("signal") == "HOLD":
            return False
        return True

class BotRunner:
    def __init__(self, prisma: Prisma, bot_id: int):
        self.prisma = prisma
        self.bot_id = bot_id
        self._running = True
        self.risk = RiskManager()

    async def load_bot(self):
        bot = await self.prisma.botrun.find_unique(where={"id": self.bot_id})
        if not bot:
            raise ValueError("Bot not found")
        return bot

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
    async def fetch_ohlcv(self, exchange, symbol: str, timeframe: str):
        return exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=150)

    async def run_loop(self):
        bot = await self.load_bot()
        strategy = StrategyRegistry.create(bot.strategy)
        exchange = await ExchangeConnector.for_exchange("binance")  # Could map per bot
        symbol = bot.symbol
        timeframe = bot.timeframe
        while self._running:
            bot_state = await self.prisma.botrun.find_unique(where={"id": self.bot_id})
            if bot_state.status != "RUNNING":
                break
            ohlcv = await asyncio.to_thread(self.fetch_ohlcv, exchange, symbol, timeframe)
            closes = [c[4] for c in ohlcv]
            ticker_data = {"closes": closes}
            context = {"symbol": symbol, "timeframe": timeframe}
            decision = strategy.execute(ticker_data, context)
            allowed = await self.risk.assess(context, decision)
            if allowed and decision["signal"] in ("BUY", "SELL"):
                qty = 0.001  # Fixed fraction (stub position sizing)
                await self.record_trade(decision["signal"], qty, closes[-1], decision)
            await asyncio.sleep(5)

    async def record_trade(self, side: str, quantity: float, price: float, decision):
        pnl = 0.0  # For simplicity
        await self.prisma.tradelog.create(data={
            "botRunId": self.bot_id,
            "side": side,
            "quantity": quantity,
            "price": price,
            "pnl": pnl
        })