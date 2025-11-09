# ROADMAP

## Phase 1: Foundation & Security (เสร็จ)
- Monorepo โครงสร้าง
- FastAPI + Prisma + Postgres
- Celery Worker
- Encrypted Exchange Keys (AES-GCM)
- Strategy Interface + RSI_CROSS

## Phase 2: Strategy Engine & Risk (เสร็จแล้ว)
- **Summary**: [PHASE2_SUMMARY.md](PHASE2_SUMMARY.md)
- **Guide**: [PHASE2_GUIDE.md](PHASE2_GUIDE.md)
- เพิ่ม MeanReversion, Breakout, VWAP
- เพิ่ม Risk Manager: Max Drawdown Tracker, Circuit Breaker
- เพิ่ม Streaming Market Data (WebSocket)
- Logging & Metrics (Prometheus + Grafana)

## Phase 3: i18n Dashboard & Auth (เสร็จแล้ว ✅)
- **Summary**: [PHASE3_SUMMARY.md](PHASE3_SUMMARY.md)
- **Guide**: [PHASE3_GUIDE.md](PHASE3_GUIDE.md)
- ✅ Google OAuth Integration
- ✅ Telegram Link & Notification
- ✅ Dynamic Theme / Config GUI
- ✅ เพิ่มภาษาใหม่ (จีน, ญี่ปุ่น)

## Phase 4: Advanced Risk & Monetization (กำลังดำเนินการ 🚧)
- **Summary**: [PHASE4_SUMMARY.md](PHASE4_SUMMARY.md)
- **Guide**: [PHASE4_GUIDE.md](PHASE4_GUIDE.md)
- PromptPay Top-up Flow (QR / Callback)
- Rental Contract Expiry Enforcement
- Module Plugin Loader (Entry Point)
- Portfolio Aggregation / Multi-Account
- Backtester / Paper Trading Mode

## Phase 5: Compliance & Audit
- เพิ่ม Audit Trail ทุก API
- Static Code Scan (Bandit, Semgrep)
- Secret Rotation Flow
- DR/Failover Strategy (Multi-region)

## Phase 6: ML / Intelligence (เสริม)
- Signal Quality Scoring
- Reinforcement Strategy Tuning
- Predictive Volatility Estimation