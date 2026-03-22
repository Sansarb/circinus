# Options Quant System

Implementation-ready v1 multi-agent options trading framework.

## What is included
- Market data agent
- Feature engineering agent
- Regime detection agent
- Signal generation agent
- Risk agent
- Execution agent (paper/live stub)
- Journal agent
- Optimizer agent
- Orchestrator
- Simple CLI runner

## Quick start

```bash
python main.py
```

## Next production upgrades
- Replace `MarketDataAgent` stub with IBKR or Polygon data adapter
- Replace `ExecutionAgent` with live broker routing
- Persist journal to SQLite/Postgres
- Add Greeks and real option chain selection
- Add backtest engine
