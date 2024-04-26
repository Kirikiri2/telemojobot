import telebot
from telebot import types
bot = telebot.TeleBot('6315152427:AAFDco_qQgHRHkw5bxXfXfAPmoU5sHIaeCU') #Нашен токен

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"✌️Peace, {message.from_user.first_name} {message.from_user.last_name}")
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    markup.add(button_yes)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
bot.infinity_polling()