"""
В данном файле можно в переменной передать параметры кнопок: ReplyKeyboardMarkup, InlineKeyboardButton
Чтобы не 'загрязнять' файл handlers.py
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='кто я?'), KeyboardButton(text='инструкция')],
    [KeyboardButton(text='заполнить данные'), KeyboardButton(text='помощь')]
], input_field_placeholder='Выберите пункт')

hello_from_bot = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='инструкция'), KeyboardButton(text='заполнить данные')],
    [KeyboardButton(text='помощь'), KeyboardButton(text='перезагрузка')]
], input_field_placeholder='Выберите пункт')

instruction = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='заполнить данные'), KeyboardButton(text='пример')],
    [KeyboardButton(text='перезагрузка'), KeyboardButton(text='перезагрузка')]
], input_field_placeholder='Выберите пункт')

example = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='заполнить данные'), KeyboardButton(text='инструкция')],
    [KeyboardButton(text='помощь'), KeyboardButton(text='перезагрузка')]
], input_field_placeholder='Выберите пункт')

help_user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='инструкция'), KeyboardButton(text='пример')],
    [KeyboardButton(text='помощь'), KeyboardButton(text='перезагрузка')]
], input_field_placeholder='Выберите пункт')

