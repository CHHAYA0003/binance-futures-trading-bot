import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing {order_type} order | {symbol} | {side} | Qty: {quantity} | Price: {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order Success | ID: {order['orderId']} | Status: {order['status']}")
        return order

    except Exception as e:
        logging.error(f"Order Failed | Error: {str(e)}")
        raise
