"""// ZeaZDev [Backend Celery Tasks] //
// Project: Auto Bot Trader i18n //
// Version: 1.0.0 (Omega Scaffolding) //
// Author: ZeaZDev Meta-Intelligence (Generated) //
// --- DO NOT EDIT HEADER --- //"""
import asyncio
import os
from celery import shared_task
from prisma import Prisma
from src.trading.bot_runner import BotRunner

prisma = Prisma()

@shared_task(bind=True, name="run_bot_loop")
def run_bot_loop(self, bot_id: int):
    asyncio.run(run_bot_async(bot_id))

async def run_bot_async(bot_id: int):
    await prisma.connect()
    runner = BotRunner(prisma=prisma, bot_id=bot_id)
    await runner.run_loop()
    await prisma.disconnect()