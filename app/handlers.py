from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import MotoristBot.app.buttons as kb

from MotoristBot.app.texts import HelloFromBot, Instruction, Example, Help

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветcтвую дорогой, {message.from_user.full_name}!", reply_markup=kb.start)


@router.message(F.text == "перезагрузка")
async def get_hello(message: Message):
    await message.answer(f"Давайте с самого начала, {message.from_user.full_name}!", reply_markup=kb.hello_from_bot)


@router.message(F.text == "кто я?")
async def get_hello(message: Message):
    text = HelloFromBot.hello()
    await message.answer(text, reply_markup=kb.hello_from_bot)


@router.message(F.text == "инструкция")
async def get_info(message: Message):
    text = Instruction.get_ins()
    await message.answer(text, reply_markup=kb.instruction)


@router.message(F.text == "пример")
async def get_example(message: Message):
    text = Example.get_example()
    await message.answer(text, reply_markup=kb.example)


@router.message(F.text == "помощь")
async def get_help(message: Message):
    text = Help.get_help()
    await message.answer(text, reply_markup=kb.help_user)




