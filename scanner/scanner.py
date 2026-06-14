from exchange.bybit_client import BybitClient

class MarketScanner:
    def __init__(self):
        self.client = BybitClient()

    def scan(self):
        """
        Returns filtered market data for scoring
        """
        tickers = self.client.get_tickers()

        filtered = []

        for t in tickers:
            try:
                symbol = t.get("symbol")
                price = t.get("price")
                volume = t.get("volume") or 0
                change = t.get("change") or 0

                # basic filters
                if not symbol or price is None:
                    continue

                if volume < 1_000_000:
                    continue

                # momentum proxy
                momentum = max(0, change or 0)

                filtered.append({
                    "symbol": symbol,
                    "price": price,
                    "volume": volume,
                    "momentum": momentum / 10,
                    "breakout": 0.5 if momentum > 2 else 0,
                    "orderbook": 0.5,
                    "risk": 0.2 if momentum > 5 else 0.1
                })

            except Exception:
                continue

        return filtered