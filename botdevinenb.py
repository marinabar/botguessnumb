import telebot
import random
token = "561568815:AAE3kTf7n2apXhUFvLndnyxlWmbVffcvEm0"
notes={}
# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5://tvorogme@tvorog.me:6666'}

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    user_id = message.chat.id
    if user_id not in notes:
        nb=random.randint(0, 50)
        bot.send_message(user_id, "I chose a number from 1 to 50")
        notes[user_id]=nb
    else:
        if int(text) > notes[user_id]:
            bot.send_message(user_id, "-")
        elif int(text) < notes[user_id]:
            bot.send_message(user_id, "+")
        else:
            bot.send_message(user, "Well done, let's try another time")
            nb=random.randint(0, 50)
            notes[user_id]=nb
bot.polling(none_stop=True)
