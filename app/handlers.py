from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import MotoristBot.app.buttons as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)


@router.message(Command('example'))
async def get_help(message: Message):
    text = Example.get_example()
    await message.answer(text, reply_markup=kb.main)


@router.message(Command('instruction'))
async def get_help(message: Message):
    text = Instruction.get_ins()
    await message.answer(text, reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    text = Help.get_help()
    await message.answer(text, reply_markup=kb.main)


@router.message(Command('GetQRcode'))
async def get_qr(message: Message):
    await message.answer('Жду текст!', reply_markup=kb.main1)

    @router.message(F.text)
    async def get_help(message: Message):
        data = message.text
        Getpng().create_qrcode(data)
        file = types.FSInputFile('qr_code.png', 'rb')
        await message.answer_photo(photo=file)


@router.message(F.text == "Ты тут?")
async def are_u_here(message: Message):
    await message.reply('Да, я тут!')

# @router.message(F.text)
# async def get_help(message: Message):
#     # sens = message.text.split(' ')
#     # name, data = sens
#     data = message.text
#     Getpng().create_qrcode(data)
#     # with open('qr_code.png', 'rb') as photo:
#     await message.answer_photo(photo=types.FSInputFile('qr_code.png', 'rb'))
#         # await message.answer_photo(photo)
