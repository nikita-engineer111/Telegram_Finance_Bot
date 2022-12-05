# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import standart_responses
import category
import purchase
# bot init

bot = Bot(token="")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(massage: types.Message):
    response = ''
    if massage.text == '/start':
        response = standart_responses.start_response(massage.from_user.full_name)
    elif massage.text == '/help':
        response = standart_responses.help_response()
    elif massage.text == '/add_purchase':
        response = standart_responses.add_purchase()
    elif massage.text == '/show_statistics':
        response = standart_responses.show_statistics()
    elif massage.text == '/create_category':
        response = standart_responses.create_category()
    elif massage.text == '/show_categories':
        response = category.show_categories()

    elif '/add_purchase' in massage.text:
        response = purchase.add_purchase(massage.text)
    elif '/show_statistics' in massage.text:
        pass
    elif '/create_category' in massage.text:
        response = category.create_category(massage.text)

    else:
        response = standart_responses.trash()
    await massage.answer(response)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
