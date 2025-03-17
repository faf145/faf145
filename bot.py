import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = "7942350287:AAFHewt2FBcZmKgFw41sfQREWSfh3CPIKFY"  # Замени на свой токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ASCII-мэппинг для букв
ASCII_MAP = {
    "А": "  /\\  \n /  \\ \n/____\\\n|    |\n|    |",
    "Б": " ____ \n|    |\n|____|\n|    |\n|____|",
    "В": "____  \n|   \\ \n|___/ \n|   \\ \n|___/ ",
    "Г": "_____ \n|     \n|     \n|     \n|     ",
    "Д": "  ___  \n /   \\ \n|     |\n|_____|",
    "Е": "_____ \n|     \n|___  \n|     \n|____|",
    "Ж": "|\\  /|\n \\ / \n  |  \n / \\ \n|/  \\|",
    "З": " ____ \n    / \n  --  \n    \\ \n ____ ",
    "И": "|\\   |\n| \\  |\n|  \\ |\n|   \\|\n|    |",
    "К": "|  / \n| /  \n||   \n| \\  \n|  \\ ",
    "Л": "  ___  \n /   \\ \n|     |\n|     |\n|     |",
    "М": "|\\   /|\n| \\_/ |\n|     |\n|     |\n|     |",
    "Н": "|    |\n|    |\n|____|\n|    |\n|    |",
    "О": " ____ \n|    |\n|    |\n|    |\n|____|",
    "П": " ____ \n|    |\n|    |\n|    |\n|    |",
    "Р": "____  \n|   \\ \n|___/ \n|     \n|     ",
    "С": " ____ \n|     \n|     \n|     \n|____ ",
    "Т": "_____ \n  |   \n  |   \n  |   \n  |   ",
    "У": "\\    /\n \\  / \n  ||  \n  ||  \n  ||  ",
    "Ф": "  ||  \n /||\\ \n  ||  \n  ||  \n  ||  ",
    "Х": "\\    /\n \\  / \n  ||  \n /  \\ \n/    \\",
    "Ч": "|    |\n|    |\n|____|\n     |\n     |",
    "Ш": "| | | |\n| | | |\n| |_| |\n|     |\n|     |",
    "Щ": "| | | |\n| | | |\n| |_| |\n|   | |\n|   |_|",
    "Ы": "|    |\n|    |\n|____|\n|    |\n|____|",
    "Ь": "|    \n|    \n|___ \n|    |\n|____|",
    "Э": " ____ \n    / \n --  \n    \\ \n____/ ",
    "Ю": "|  ___\n| |   |\n| |___|\n| |   |\n|_|___|",
    "Я": " ____ \n|    |\n|____|\n|    |\n|    |",
}

# Функция для конвертации текста в ASCII-арт
def text_to_ascii(text):
    lines = ["", "", "", "", ""]
    for char in text.upper():
        if char in ASCII_MAP:
            ascii_letter = ASCII_MAP[char].split("\n")
            for i in range(5):
                lines[i] += ascii_letter[i] + "  "
        else:
            for i in range(5):
                lines[i] += "     "  # Пустое пространство для неизвестных символов
    return "\n".join(lines)

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Напиши любое слово, и я нарисую его!")

# Обработчик текста
@dp.message()
async def send_ascii(message: Message):
    text = message.text
    ascii_art = text_to_ascii(text)
    await message.answer(f"<pre>{ascii_art}</pre>", parse_mode="HTML")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
