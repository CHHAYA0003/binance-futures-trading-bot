# Binance Futures Testnet Trading Bot

A command-line based trading bot built using Python that interacts with the Binance Futures Testnet API.



Project Features

- Place MARKET orders  
- Place LIMIT orders  
- Check account balance  
- View open positions  
- Close open positions  
- Get symbol trading information  
- Input validation  
- Order confirmation before execution  
- Quantity safety limit  
- Logging enabled  
- Modular project structure  



Tech Stack

- Python 3.11  
- python-binance  
- python-dotenv  
- REST API  
- CLI-based interface  



Project Structure

bot/
    client.py
    orders.py
    account.py
    position.py
    validators.py
    info.py
    logging_config.py

cli.py  
requirements.txt  
.env (not included in repository)



Setup Instructions

1. Clone Repository

git clone https://github.com/CHHAYA0003/binance-futures-trading-bot.git  
cd binance-futures-trading-bot  

2. Install Dependencies

pip install -r requirements.txt  

3. Create .env file in root directory

API_KEY=your_api_key  
API_SECRET=your_api_secret  


Usage Examples

Place Market Order

python cli.py --mode order --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002  

Place Limit Order

python cli.py --mode order --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 65000  

Check Account Balance

python cli.py --mode balance  

View Open Positions

python cli.py --mode positions  

Close Position

python cli.py --mode close --symbol BTCUSDT  

Get Symbol Info

python cli.py --mode info --symbol BTCUSDT  



Assumptions

- Using Binance Futures Testnet  
- API keys stored securely in .env file  
- Minimum order notional must be greater than or equal to 100 USDT  
- Quantity and price precision must match exchange rules  



Safety Mechanisms

- Quantity safety limit  
- Order confirmation prompt  
- Input validation  
- Exception handling  
- Logging support  


