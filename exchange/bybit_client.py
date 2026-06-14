class BybitClient:
    def __init__(self):
        self.name = "bybit"

    def get_tickers(self):
        return []

    def get_orderbook(self, symbol):
        return {}

    def place_order(self, symbol, side, amount):
        print(f"Order: {side} {symbol} {amount}")
        return True