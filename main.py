import telebot


token = ''
bot = telebot.TeleBot()

@bot.message_handler(commands= ['start'])
def welcome(message):
    id = message.chat.id
    bot.send_message(id, 'Приветствую')
   
bot.polling()
