import telebot
import config
import functions
import models
import text


bot = telebot.TeleBot(config.tg_token)

@bot.message_handler(commands= ['start'])
def welcome(message):
    id = message.chat.id
    bot.send_message(id, 'Приветствую')
   
bot.polling()