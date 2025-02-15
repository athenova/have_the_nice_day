import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
# CHAT_ID = -1002374309134
CHAT_ID = '@have_the_nice_day'

def job():
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - самый оптимистичный в мире человек" },
            { "role": "user", "content": f"Пожелай отличного дня всему миру, используй смайлики" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

schedule.every().day.at("07:00",'Europe/Moscow').do(job)

fifteen_minutes = 15 * 60

for i in range(fifteen_minutes):
    schedule.run_pending()
    time.sleep(1)
