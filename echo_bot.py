
# @bot.message_handler(command=['start', 'bop'])
# def send_bop(message):
    # bot.send_message(chat_id, 'this is your token', reply_markup=['eses'])
#     bot.reply_to(message, 'this is it')
    

# bot.polling()
from flask import Flask, request
import telebot
import os

TOKEN = "746406709:AAHGsGOKxHwPOhRMdUOM5JNKsVxI2cCTbyQ"
server = Flask(__name__)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	# bot.reply_to(message, "Howdy, how are you doing?")
    chat_id = message.chat.id
    bot.send_message(chat_id, 'this is your token')

    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

# bot.polling()


#server side
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="" + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
