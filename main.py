import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = 7991412640AAGgSJNF4ry_reu62mJvvKxeWAcD5b2YAaQ

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура с кнопками Да и Нет
age_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=✅ Да, callback_data=age_yes)],
        [InlineKeyboardButton(text=❌ Нет, callback_data=age_no)]
    ]
)

@dp.message(Command(start))
async def start_command(message Message)
    await message.answer(Вам есть 18, reply_markup=age_keyboard)

@dp.callback_query(F.data == age_yes)
async def age_confirmed(callback types.CallbackQuery)
    text = (Сначала подпишитесь на наших спонсоровn
            t.meStarsovEarnBotstart=5ia9jc40onn
            Инструкцияn
            1. Зайти по ссылке и нажать СТАРТn
            2. Выполнить заданиеn
            3. Подтвердить заданиеn
            4. ОТправить скриншотn
            5. Ждать)
    await callback.message.edit_text(text)  # Изменяет предыдущее сообщение
    await callback.answer()  # Закрывает уведомление

@dp.callback_query(F.data == age_no)
async def age_denied(callback types.CallbackQuery)
    await callback.message.edit_text(Вы не можете участвовать.)
    await callback.answer()  

async def main()
    await dp.start_polling(bot)

if __name__ == __main__
    asyncio.run(main())
