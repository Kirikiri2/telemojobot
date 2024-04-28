import telebot
from telebot import types
import requests

bot = telebot.TeleBot('6315152427:AAFDco_qQgHRHkw5bxXfXfAPmoU5sHIaeCU') #Нашен токен

@bot.message_handler(commands=['start'])

def main(message):

   # bot.send_message(message.chat.id, f"✌️Peace, {message.from_user.first_name} {message.from_user.last_name}")
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь проверить статус заказа?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    markup.add(button_yes)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        agreement = "Введите номер заказа /mojo 000.000.000"
        markup = types.InlineKeyboardMarkup()
        bot.send_message(function_call.message.chat.id, agreement, reply_markup=markup)
        bot.answer_callback_query(function_call.id)
@bot.message_handler()
def id(message):
    if message.text.lower() == '/mojo 001.111.111' or message.text.lower() == '/mojo 555.111.111':
        if message.text.lower() == '/mojo 001.111.111':
            url = "https://pay-test.raif.ru/api/sbp/v1/qr/AD3D919E91494C53A41C5EFEB837846B/payment-info"

            # Заголовок с токеном авторизации
            headers = {
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJNQTYyMjk3NiIsImp0aSI6ImI1OTNkODRkLTk1MWYtNGIyZi05ZGViLTcxOWExNDM4NWVmZCJ9.si-87k3Aw5GN67orgJpoyTXC0C2OpWwRCKzLogRWawU"
            }

            # Отправка GET-запроса
            response = requests.get(url, headers=headers)

            # Проверка статуса ответа
            if response.status_code == 200:
                response_data = response.json()
                status = response_data['paymentStatus']
                if status == "SUCCESS":
                    bot.send_message(message.chat.id, "Заказ оплачен.")
                else:
                    bot.send_message(message.chat.id, "Заказ не оплачен.\nПовторите запрос для обновления статуса")
            else:
                bot.send_message(message.chat.id, "Ошибка при выполнении запроса:", response.status_code)
        if message.text.lower() == '/mojo 555.111.111':
            url = "https://pay-test.raif.ru/api/sbp/v1/qr/AD04CDC45D4B4E3EB24CD2F1FD6F84FF/payment-info"

            # Заголовок с токеном авторизации
            headers = {
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJNQTYyMjk3NiIsImp0aSI6ImI1OTNkODRkLTk1MWYtNGIyZi05ZGViLTcxOWExNDM4NWVmZCJ9.si-87k3Aw5GN67orgJpoyTXC0C2OpWwRCKzLogRWawU"
            }

            # Отправка GET-запроса
            response = requests.get(url, headers=headers)

            # Проверка статуса ответа
            if response.status_code == 200:
                response_data = response.json()
                status = response_data['paymentStatus']
                if status == "SUCCESS":
                    bot.send_message(message.chat.id, "Заказ оплачен.")
                else:
                    bot.send_message(message.chat.id, "Заказ не оплачен.\nПовторите запрос для обновления статуса")
            else:
                bot.send_message(message.chat.id, "Ошибка при выполнении запроса:", response.status_code)

    elif message.text.lower() == '/mojo 044.111.111' or message.text.lower() == '/mojo 009.111.111':
        if message.text.lower() == '/mojo 044.111.111':
            url = "https://pay-test.raif.ru/api/sbp/v1/qr/AD02D3A781054D52BFE4654CCA8CCF1D/payment-info"

            headers = {
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJNQTYyMjk3NiIsImp0aSI6ImI1OTNkODRkLTk1MWYtNGIyZi05ZGViLTcxOWExNDM4NWVmZCJ9.si-87k3Aw5GN67orgJpoyTXC0C2OpWwRCKzLogRWawU"
            }

            # Отправка GET-запроса
            response = requests.get(url, headers=headers)

            # Проверка статуса ответа
            if response.status_code == 200:
                response_data = response.json()
                status = response_data['paymentStatus']
                if status == "SUCCESS":
                    bot.send_message(message.chat.id, "Заказ оплачен.")
                else:
                    bot.send_message(message.chat.id, "Заказ не оплачен.\nПовторите запрос для обновления статуса")
            else:
                bot.send_message(message.chat.id, "Ошибка при выполнении запроса:", response.status_code)
        if message.text.lower() == '/mojo 009.111.111':
            url = "https://pay-test.raif.ru/api/sbp/v1/qr/AD4E6B5A010E4C42ADABB0FE142D092D/payment-info"

            headers = {
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJNQTYyMjk3NiIsImp0aSI6ImI1OTNkODRkLTk1MWYtNGIyZi05ZGViLTcxOWExNDM4NWVmZCJ9.si-87k3Aw5GN67orgJpoyTXC0C2OpWwRCKzLogRWawU"
            }

            # Отправка GET-запроса
            response = requests.get(url, headers=headers)

            # Проверка статуса ответа
            if response.status_code == 200:
                response_data = response.json()
                status = response_data['paymentStatus']
                if status == "SUCCESS":
                    bot.send_message(message.chat.id, "Заказ оплачен.")
                else:
                    bot.send_message(message.chat.id, "Заказ не оплачен.\nПовторите запрос для обновления статуса")
            else:
                bot.send_message(message.chat.id, "Ошибка при выполнении запроса:", response.status_code)

    else:
        bot.send_message(message.chat.id, "Неверный формат ID или незарегистированный ID.")

bot.infinity_polling()