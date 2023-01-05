from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_panel_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    keyboard=[
        [
            KeyboardButton(
                text='ЕВРОПОЧТА🐯'
            ),
            KeyboardButton(
                text='БЕЛПОЧТА😶'
            ),
        ]
    ]
)