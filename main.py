import telebot
from telebot import types

bot = telebot.TeleBot('6315152427:AAFDco_qQgHRHkw5bxXfXfAPmoU5sHIaeCU') #Нашен токен

@bot.message_handler(commands=['start'])

def main(message):

   # bot.send_message(message.chat.id, f"✌️Peace, {message.from_user.first_name} {message.from_user.last_name}")
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь проверить статус заказа?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    markup.add(button_yes)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        agreement = "Введите номер заказа"
        markup = types.InlineKeyboardMarkup()
        bot.send_message(function_call.message.chat.id, agreement, reply_markup=markup)
        bot.answer_callback_query(function_call.id)
bot.infinity_polling()