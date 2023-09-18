from settings import * 
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
data = Data()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    msg = 'Привет! Это место создано специально для тебя. Если тебе вдруг станет немного грустно или тоскливо, этот бот поможет тебе напомнить о разных прекрасных вещах!)'
    btns = [
        InlineKeyboardButton('Для тебя', callback_data='compliment'),
        InlineKeyboardButton('Мы', callback_data='photo'),
    ]
    kb = InlineKeyboardMarkup(1)
    kb.add(*btns)
    await bot.send_message(chat_id=message.chat.id, text=msg, reply_markup=kb)


@dp.callback_query_handler(text='menu')
async def start(call: types.CallbackQuery):
    msg = 'Привет! Это место создано специально для тебя. Если тебе вдруг станет немного грустно или тоскливо, этот бот поможет тебе напомнить о разных прекрасных вещах!)'
    btns = [
        InlineKeyboardButton('Для тебя', callback_data='compliment'),
        InlineKeyboardButton('Мы', callback_data='photo'),
    ]
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(*btns)
    await bot.send_message(chat_id=call.message.chat.id, text=msg, reply_markup=kb)


@dp.callback_query_handler(text='compliment')
async def compliment(call: types.CallbackQuery):
    msg = data.get_random_compliment()
    btns = [
        InlineKeyboardButton(text='Еще один!', callback_data='compliment'),
        InlineKeyboardButton(text='Назад', callback_data='menu')
    ]
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(*btns)
    await bot.send_message(chat_id=call.message.chat.id, text=msg, reply_markup=kb)


@dp.callback_query_handler(text='photo')
async def photo(call: types.CallbackQuery):
    ph = open(data.get_random_photo(), 'rb')
    btns = [
        InlineKeyboardButton(text='Еще фото!', callback_data='photo'),
        InlineKeyboardButton(text='Назад', callback_data='menu')
    ]
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(*btns)
    await bot.send_photo(call.message.chat.id, photo=ph)
    await bot.send_message(chat_id=call.message.chat.id, text="Надеюсь, что тебя хотя бы улыбнули наши фото)", reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp)