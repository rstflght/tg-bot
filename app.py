import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# Make folder for log if mot exists
if not os.path.exists("./log"):
    os.makedirs("./log")


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,
    filename = "./log/translit_bot.log"
    )

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'Time: {datetime.now()}, User: "{user_name}: id{user_id}" - Start Bot')
    await bot.send_message(chat_id=user_id, text=text)

# 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = translit(message.text)
    logging.info(f'Time: {datetime.now()}, User: "{user_name} - id{user_id}": Send: "{message.text}", Answer: "{text}"')
    await message.answer(text=text)


# traslit phrase
def translit(phrase: str) -> str:

    trans_dict = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "y",
    "ъ": "ie",
    "э": "e",
    "ю": "iu",
    "я": "ia"
    }

    back_phrase=str()
    for ch in phrase:
        if ch.isalpha() and ch.lower() in trans_dict.keys():
            if ch.isupper():
                back_phrase += trans_dict[ch.lower()].upper()
            elif ch.islower():
                back_phrase += trans_dict[ch]
        else:
            back_phrase += ch

    return back_phrase

# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)
