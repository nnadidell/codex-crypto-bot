import os
import requests
from telegram.ext import Updater, CommandHandler

# Get token from environment
BOT_TOKEN = os.getenv('BOT_TOKEN')

def get_price(coin):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data.get(coin, {}).get('usd', 'N/A')

def price(update, context):
    coin = ' '.join(context.args).lower()
    if not coin:
        update.message.reply_text("Please send a coin name, e.g., /price dogecoin")
        return
    price = get_price(coin)
    update.message.reply_text(f'{coin.upper()} price: ${price}')

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("price", price))

updater.start_polling()
updater.idle()
