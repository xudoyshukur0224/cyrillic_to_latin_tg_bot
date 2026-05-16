import telebot
from transliterate import to_cyrillic, to_latin
TOKEN = "8821716042:AAHhthkepFu_eeJAcvkASeIigtbeHoxST6c" 
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, botimizga xush kelibsiz")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text
    if text.isascii():    
        bot.reply_to(message, to_cyrillic(text))
    else:
        bot.reply_to(message, to_latin(text))


bot.infinity_polling()


# cyrillic_to_latin_converter_bot 
# cyrillic_latin_converter_bot +