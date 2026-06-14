def calculate_score(market_data):
    """
    Returns score 0-100
    """
    score = 0

    # placeholder logic
    score += market_data.get('momentum', 0) * 30
    score += market_data.get('volume', 0) * 25
    score += market_data.get('breakout', 0) * 20
    score += market_data.get('orderbook', 0) * 15

    risk = market_data.get('risk', 0)
    score -= risk * 10

    return max(0, min(100, score))