from aiogram import types, Dispatcher


async def echo(message: types.Message):
    text = [
        'Эхо без состояния.',
        'Сообщение:',
        message.text
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)
