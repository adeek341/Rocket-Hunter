from config import STOP_LOSS_PERCENT, TAKE_PROFIT_TARGETS, TRAILING_START_PERCENT

class ExitLogic:
    def __init__(self):
        pass

    def evaluate(self, position):
        """
        Returns: 'SELL' or None
        """

        pnl = position.pnl_percent

        # STOP LOSS
        if pnl <= -STOP_LOSS_PERCENT:
            return "SELL"

        # TAKE PROFIT
        for tp in TAKE_PROFIT_TARGETS:
            if pnl >= tp:
                return "SELL"

        # SIMPLE TRAILING EXIT
        if pnl >= TRAILING_START_PERCENT:
            if position.current_price < position.entry_price:
                return "SELL"

        return None