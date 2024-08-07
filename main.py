import telebot

bot = telebot.TeleBot('7355895428:AAFWYVjErBfLTHMnJuE5CPpW8Ao7SEmhRK4')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Давайте начнем', parse_mode='Markdown')


@bot.message_handler(commands=['command1'])
def main1(message):
    bot.send_message(message.chat.id, '[Расписание](https://www.asu.ru/timetable/)', parse_mode='Markdown')


@bot.message_handler(commands=['command2'])
def main2(message):
    bot.send_message(message.chat.id, '[Личный кабинет](https://lk.asu.ru/)', parse_mode='Markdown')


bot.infinity_polling()
