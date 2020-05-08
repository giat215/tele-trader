from flask import Flask, request
import os
from config import *


server = Flask(__name__)


@server.route('/'+ TOKEN, methods=['POST'])
def getMessage():
    request_object = request.stream.read().decode("utf-8")
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return "got Message bro"



@server.route("/")
def pay():
    return "This is the fcx trading bot you can reach me @FCX_trading_bot on telegram"

@server.route('/hook')
def webhook():
    url=https://litecash.herokuapp.com
    bot.remove_webhook()
    bot.set_webhook(url + TOKEN)
    return f"Webhook set to {url}"

@server.route('/')
def index():
    url=https://litecash.herokuapp.com
    return f"To set webhook goto to <a href='{url}hook'>{url}hook</a>"

# bot.remove_webhook()
# bot.polling()

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
