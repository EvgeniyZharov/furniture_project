from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# TOKEN = "token"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def create_keyboards(btn_list):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for elem in btn_list:
        kb.add(KeyboardButton(elem))
    return kb


QA = {
    "Как заказать консультацию?": "Позвоните по номеру 8хххххх хххх, Вам все расскажут",
    "Как заказать замеры": "Позвоните, чтобы договориться о временном слоте для замеров мебели",
    "Как оплатить": "Принимаем карты и наличные"
}


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nБот работы с мебелью!",
                        reply_markup=create_keyboards(btn_list=list(QA.keys())))


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text in QA:
        await bot.send_message(msg.from_user.id, QA[msg.text])
    else:
        await bot.send_message(msg.from_user.id, "Я не знаю что на это ответить. Передаю сообщение администратору")


if __name__ == '__main__':
    print("ok")

    executor.start_polling(dp)
