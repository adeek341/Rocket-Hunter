import time
from scanner.scanner import MarketScanner
from strategy.scoring import calculate_score
from strategy.entry_logic import EntryLogic
from risk.risk_manager import RiskManager
from execution.trader import Trader
from config import SCAN_INTERVAL_SECONDS

class RocketHunter:
    def __init__(self):
        self.scanner = MarketScanner()
        self.entry = EntryLogic()
        self.risk = RiskManager()
        self.trader = Trader()
        self.balance = 100

    def run_cycle(self):
        assets = self.scanner.scan()

        scored_assets = []
        for a in assets:
            score = calculate_score(a)
            scored_assets.append({
                "symbol": a["symbol"],
                "score": score
            })

        signals = self.entry.evaluate(scored_assets)

        for s in signals:
            if not self.risk.can_trade():
                continue

            amount = self.risk.size_position(self.balance)

            print(f"TRADE {s['symbol']} score={s['score']} action={s['action']}")

            self.trader.buy(s["symbol"], amount)

    def run(self):
        print("Rocket Hunter v1 LIVE")

        while True:
            try:
                self.run_cycle()
                time.sleep(SCAN_INTERVAL_SECONDS)
            except Exception as e:
                print("error:", e)
                time.sleep(5)


if __name__ == "__main__":
    RocketHunter().run()