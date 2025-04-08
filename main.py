from telegram import Bot
from telegram.ext import Updater, CommandHandler
import os

# Токен твоего бота
TELEGRAM_TOKEN = "8195654780:AAFv-qllZ8d-t3JcczwQcnUFcL7akbKQdk8"

# Пример сигнала
signal = """
[Whale Signal]
Amber Group перевела 12.5M USDT на Binance.
Актив: BTC
Цена сейчас: $66,840

Комментарий:
Кит готовится к закупке — рынок ещё не среагировал.
Вход возможен прямо сейчас или на откате -0.5%.
Стоп: -2%. Цель: +6–10%.
"""

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ Бот работает. Жди сигналов.")
    context.bot.send_message(chat_id=update.effective_chat.id, text=signal)

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

import threading
import time
import requests
from bs4 import BeautifulSoup

def check_whale_alert():
    while True:
        try:
            url = "https://nitter.net/lookonchain"  # зеркало Twitter без авторизации
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, 'html.parser')
            tweets = soup.find_all('div', {'class': 'timeline-item'})

            if not tweets:
                print("Нет твитов.")
                time.sleep(60)
                continue

            latest = tweets[0].text
            if "deposited" in latest.lower() and ("binance" in latest.lower() or "okx" in latest.lower()):
                message = "[Whale Alert Detected]\n" + latest.strip()
                print("Сигнал найден! Отправка...")
                bot.send_message(chat_id=chat_id, text=message)

            time.sleep(60)  # проверять раз в минуту
        except Exception as e:
            print("Ошибка при парсинге:", e)
            time.sleep(60)

# стартуем в фоновом
threading.Thread(target=check_whale_alert, daemon=True).start()