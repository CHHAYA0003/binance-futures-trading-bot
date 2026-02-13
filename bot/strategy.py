def simple_strategy(client, symbol):
    klines = client.futures_klines(symbol=symbol, interval="1m", limit=50)
    closes = [float(k[4]) for k in klines]

    if closes[-1] > sum(closes[-10:]) / 10:
        return "BUY"
    else:
        return "SELL"
