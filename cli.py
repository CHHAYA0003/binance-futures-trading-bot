import argparse
import sys
import traceback
    

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging
from bot.account import get_balance
from bot.position import get_positions
from bot.info import get_symbol_info 
from datetime import datetime


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol")
    parser.add_argument("--side", choices=["BUY", "SELL"])
    parser.add_argument("--type", choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--mode", required=True,
                        choices=["order", "balance", "info", "positions", "close"])

    args = parser.parse_args()

    client = get_client()

    try:

        # ================= ORDER MODE =================
        if args.mode == "order":

            if not all([args.symbol, args.side, args.type, args.quantity]):
                print("Missing required order arguments")
                sys.exit(1)

            if args.quantity > 0.01:
                print("Quantity too large for safety limit")
                sys.exit(1)

            validate_order(
                args.symbol,
                args.side,
                args.type,
                args.quantity,
                args.price
            )

            confirm = input(
                f"\nConfirm Order? {args.side} {args.quantity} {args.symbol} ({args.type}) (yes/no): "
            )

            if confirm.lower() != "yes":
                print("Order cancelled.")
                return

            order = place_order(
                client,
                args.symbol.upper(),
                args.side.upper(),
                args.type.upper(),
                args.quantity,
                args.price
            )

            print("\n===== ORDER RESPONSE =====")
            print(f"[{datetime.now()}] Order ID:", order.get("orderId"))
            print("Status:", order.get("status"))
            print("Executed Qty:", order.get("executedQty"))
            print("Avg Price:", order.get("avgPrice"))
            print("==========================\n")

        # ================= BALANCE MODE =================
        elif args.mode == "balance":

            balance = get_balance(client)
            print("\n===== ACCOUNT BALANCE =====")
            print("Available Balance:", balance)
            print("===========================\n")

        # ================= POSITIONS MODE =================
        elif args.mode == "positions":

            positions = get_positions(client)

            print("\n===== OPEN POSITIONS =====")
            if not positions:
                print("No open positions.")
            else:
                for p in positions:
                    print(p)
            print("==========================\n")

        # ================= CLOSE MODE =================
        elif args.mode == "close":

            if not args.symbol:
                print("Symbol required to close position")
                sys.exit(1)

            positions = get_positions(client)

            for p in positions:
                if p["symbol"] == args.symbol.upper() and float(p["positionAmt"]) != 0:

                    qty = abs(float(p["positionAmt"]))
                    side = "SELL" if float(p["positionAmt"]) > 0 else "BUY"

                    close_order = place_order(
                        client,
                        args.symbol.upper(),
                        side,
                        "MARKET",
                        qty
                    )

                    print("\n===== POSITION CLOSED =====")
                    print("Order ID:", close_order.get("orderId"))
                    print("============================\n")
                    return

            print("No open position found for", args.symbol)

        # ================= INFO MODE =================
        elif args.mode == "info":

            if not args.symbol:
                print("Symbol required for info mode")
                sys.exit(1)

            info = get_symbol_info(client, args.symbol)

            print("\n===== SYMBOL INFO =====")
            if info:
                for k, v in info.items():
                    print(f"{k}: {v}")
            else:
                print("Symbol not found")
            print("=======================\n")

    except Exception as e:
     print("\n ERROR:", str(e))
     traceback.print_exc()
     sys.exit(1)


if __name__ == "__main__":
    main()

