import telebot

bot = telebot.TeleBot('6315152427:AAFDco_qQgHRHkw5bxXfXfAPmoU5sHIaeCU')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name} {message.from_user.last_name}")

bot.infinity_polling()













