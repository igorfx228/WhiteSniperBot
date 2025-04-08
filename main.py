from telegram import Bot
from telegram.ext import Updater, CommandHandler
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

signal_example = """[Whale Signal]
Amber Group перевела 9.2M USDT на Binance.
Актив: ETH
Цена сейчас: $3,185

Комментарий:
Кит завёл стейблы на биржу → будет закупка.
Цена ещё не пошла → ты успеваешь зайти.
Зайди в ETH сейчас или на лёгкой просадке (-0.5%).
Стоп: -2% от цены. Цель: +5–10%."""

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бот активен. Ожидай сигналы.")
    context.bot.send_message(chat_id=update.effective_chat.id, text=signal_example)

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
