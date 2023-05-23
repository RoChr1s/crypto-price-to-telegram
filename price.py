import requests
import json
import time

# Replace YOUR_API_KEY and YOUR_CHAT_ID with your actual Telegram bot API key and chat ID
telegram_api_key = 'YOUR_API_KEY'
telegram_chat_id = 'YOUR_CHAT_ID'

# Define the endpoint URL for the Binance public REST API
binance_url = 'https://api.binance.com/api/v3/ticker/price'

# Define the symbols for the trading pairs as a list of strings
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']

# Define the interval for fetching the price (in seconds)
interval = 900  # 15 minutes

# Define a function to send a message to the Telegram bot
def send_message(message):
    telegram_url = f'https://api.telegram.org/bot{telegram_api_key}/sendMessage'
    payload = {'chat_id': telegram_chat_id, 'text': message}
    response = requests.post(telegram_url, data=payload)
    return response.json()

# Define a function to fetch the price for a given symbol from Binance
def get_price(symbol):
    params = {'symbol': symbol}
    response = requests.get(binance_url, params=params)
    return float(json.loads(response.content)['price'])

# Define a loop that fetches the prices and sends them to the Telegram bot every 15 minutes
while True:
    message = ''
    for symbol in symbols:
        price = get_price(symbol)
        message += f'{symbol} price: {format(price, ",.2f")}\n'
    send_message(message)
    time.sleep(interval)
