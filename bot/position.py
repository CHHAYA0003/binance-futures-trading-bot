def get_positions(client):
    positions = client.futures_position_information()

    open_positions = []

    for pos in positions:
        if float(pos["positionAmt"]) != 0:
            open_positions.append({
                "symbol": pos["symbol"],
                "positionAmt": pos["positionAmt"],
                "entryPrice": pos["entryPrice"],
                "unRealizedProfit": pos["unRealizedProfit"]
            })

    return open_positions
