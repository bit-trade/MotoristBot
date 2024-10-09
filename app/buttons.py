from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/инструкция'), KeyboardButton(text='/заполнить данные')],
    [KeyboardButton(text='/ещё кнопка'), KeyboardButton(text='/помощь')]
], input_field_placeholder='Выберите пункт')

main1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/инструкция'), KeyboardButton(text='/заполнить данные')],
    [KeyboardButton(text='/ещё кнопка'), KeyboardButton(text='/помощь')]
], input_field_placeholder='Выберите пункт')

