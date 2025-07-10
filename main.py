import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("НОКИС - ШЫМБАЙ")
    btn2 = telebot.types.KeyboardButton("ШЫМБАЙ - НОКИС")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '''
НОКИСТЕН - ШЫМБАЙГА

🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄

ШЫМБАЙДАН - НОКИСКЕ

ТАКСИ ХИЗМЕТИ  24/7

📦 АМАНАТ ПОЧТА АЛЫП КЕТЕМИЗ!

ИСЕНИМЛИ, ҚОЛАЙ, ХӘМ АРЗАН

СТАРТ ТУЙМЕСИН БАСЫП ТЕКҒАНА ҚОҢЫРАУ ЕТИҢ

👇👇👇👇👇👇👇👇👇👇

📞 +998770149797
📞 +998770149797
''', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "НОКИС - ШЫМБАЙ":
        bot.send_message(message.chat.id, '''
Н О К И С Т Е Н 

⤵️⤵️⤵️⤵️⤵️⤵️⤵️

ШЫМБАЙГА ЖУРЕМИЗ 

АМАНАТ БОЛСА АЛЫП КЕТЕМИЗ

☎️ +998770149797
☎️ +998770149797
''')
    elif message.text == "ШЫМБАЙ - НОКИС":
        bot.send_message(message.chat.id, '''
Ш Ы М Б А Й Д А Н 

⤵️⤵️⤵️⤵️⤵️⤵️⤵️

НОКИСКЕ ЖУРЕМИЗ 

АМАНАТ БОЛСА АЛЫП КЕТЕМИЗ

☎️ +998770149797
☎️ +998770149797
''')
    else:
        bot.send_message(message.chat.id, "БИЗДИ ТАНЛАҒАНЫҢЫЗ УШЫН РАХМЕТ !")

bot.polling()
