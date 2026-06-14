class Position:
    def __init__(self, symbol, entry_price, amount):
        self.symbol = symbol
        self.entry_price = entry_price
        self.amount = amount
        self.current_price = 0.0
        self.pnl_percent = 0.0

class PositionManager:
    def __init__(self):
        self.positions = {}

    def add_position(self, symbol, entry_price, amount):
        self.positions[symbol] = Position(symbol, entry_price, amount)

    def update_price(self, symbol, price):
        if symbol not in self.positions:
            return

        pos = self.positions[symbol]
        pos.current_price = price
        pos.pnl_percent = ((price - pos.entry_price) / pos.entry_price) * 100

    def remove_position(self, symbol):
        if symbol in self.positions:
            del self.positions[symbol]

    def get_open_positions(self):
        return list(self.positions.values())