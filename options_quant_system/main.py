from __future__ import annotations

import json

from agents.execution import ExecutionAgent
from agents.feature import FeatureAgent
from agents.journal import JournalAgent
from agents.market_data import MarketDataAgent
from agents.optimizer import OptimizerAgent
from agents.regime import RegimeAgent
from agents.risk import RiskAgent
from agents.signal import SignalAgent
from config.settings import SETTINGS
from models.domain import PortfolioState
from orchestrator.trading_orchestrator import TradingOrchestrator


def build_orchestrator() -> TradingOrchestrator:
    return TradingOrchestrator(
        market_data_agent=MarketDataAgent(),
        feature_agent=FeatureAgent(),
        regime_agent=RegimeAgent(),
        signal_agent=SignalAgent(),
        risk_agent=RiskAgent(
            risk_per_trade_pct=SETTINGS.risk_per_trade_pct,
            max_portfolio_risk_pct=SETTINGS.max_portfolio_risk_pct,
        ),
        execution_agent=ExecutionAgent(paper=SETTINGS.paper_trading),
        journal_agent=JournalAgent(),
        optimizer_agent=OptimizerAgent(),
    )


def main() -> None:
    universe = ["SPY", "QQQ", "NVDA", "AMD", "MSFT", "AAPL"]
    portfolio = PortfolioState(capital=50000, open_risk=0.0, daily_pnl=0.0, positions=[])

    orchestrator = build_orchestrator()
    results = orchestrator.run(universe, portfolio)

    print("\n=== REGIMES ===")
    for symbol, regime in results["regimes"].items():
        print(symbol, regime)

    print("\n=== TRADE IDEAS ===")
    for idea in results["trade_ideas"]:
        print(idea["symbol"], idea["strategy"], "-", idea["rationale"])

    print("\n=== EXECUTIONS ===")
    for report in results["executions"]:
        print(report["symbol"], report["strategy"], report["status"], "-", report["message"])

    print("\n=== OPTIMIZER SUMMARY ===")
    print(json.dumps(results["optimization_summary"], indent=2))


if __name__ == "__main__":
    main()
