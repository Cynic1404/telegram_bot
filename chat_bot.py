import telebot
from gpt import ask_gpt
from credentials import bot_token

bot = telebot.TeleBot(bot_token)

messages=[]

@bot.message_handler(commands=['new_chat', 'start'])
def first_message(message):
    global messages
    messages = []
    sent_msg = bot.reply_to(message, "Welcome! what's your question? ")
    bot.register_next_step_handler(sent_msg, echo_all)



@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    user_message=message.text
    messages.append({"role": "user", "content": user_message})
    reply = ask_gpt(messages)
    messages.append({"role":"assistant", "content":reply})
    bot.reply_to(message, reply)



bot.infinity_polling()