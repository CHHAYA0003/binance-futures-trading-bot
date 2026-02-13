def get_balance(client):
    balances = client.futures_account_balance()

    for balance in balances:
        if balance["asset"] == "USDT":
            return {
                "balance": balance["balance"],
                "available": balance["availableBalance"]
            }

    return None
