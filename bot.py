import os
from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
from code_generator import generate_code

# Загружаем переменные окружения из .env файла
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Функция для обработки команды /start
async def start(update: Update, context) -> None:
    await update.message.reply_text('Привет! Я бот для генерации кода.')

# Функция для обработки команды /generate
async def generate(update: Update, context) -> None:
    code = generate_code()
    await update.message.reply_text(f'Сгенерированный код:\n{code}')

def main() -> None:
    # Создаем экземпляр Application и передаем ему токен
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate", generate))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
