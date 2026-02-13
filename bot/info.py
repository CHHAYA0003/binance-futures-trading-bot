def get_symbol_info(client, symbol):
    info = client.futures_exchange_info()

    for s in info["symbols"]:
        if s["symbol"] == symbol.upper():
            return {
                "symbol": s["symbol"],
                "status": s["status"],
                "pricePrecision": s["pricePrecision"],
                "quantityPrecision": s["quantityPrecision"],
                "minQty": next(f["minQty"] for f in s["filters"] if f["filterType"] == "LOT_SIZE"),
                "minNotional": next(f["notional"] for f in s["filters"] if f["filterType"] == "MIN_NOTIONAL")
            }

    return None
