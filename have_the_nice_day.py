import os
import telebot
import schedule
import time
from openai import OpenAI

AI_TEXT_MODEL = 'deepseek-chat'
CHAT_TOKEN_NAME = "DEEPSEEK_API_KEY"
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@have_the_nice_day'

def job():
    client = OpenAI(api_key=os.environ.get(CHAT_TOKEN_NAME), base_url="https://api.deepseek.com")
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - самый оптимистичный в мире человек" },
            { "role": "user", "content": f"Пожелай отличного дня всему миру, используй смайлики, не используй 'Конечно'" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

#job()

if __name__ == "__main__":
    schedule.every().day.at("07:00",'Europe/Moscow').do(job)

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)
