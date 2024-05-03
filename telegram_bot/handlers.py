import json

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from aggregator.aggregator import PaymentAggregator
from database.db import MongoDBase
from telegram_bot.filters import IsFormatFieldsFilter

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")


@router.message(IsFormatFieldsFilter())
async def json_message(message: Message):
    data = json.loads(message.text)
    db = MongoDBase()
    aggregator = PaymentAggregator(data)
    result = await aggregator.aggregate_data(db)
    return await message.answer(result)


@router.message()
async def wrong_message(message: Message):
    await message.answer(
        'Допустимо отправлять только следующие запросы: \n'
        '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}\n'
        '{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}\n'
        '{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}'
    )
