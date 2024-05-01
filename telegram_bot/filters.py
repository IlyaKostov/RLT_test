import json

from aiogram.filters import Filter
from aiogram.types import Message


class IsFormatFieldsFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        try:
            data = json.loads(message.text)
            if not isinstance(data, dict):
                return False

            required_fields = ['dt_from', 'dt_upto', 'group_type']
            if not all(field in data for field in required_fields):
                return False

            group_type_field = ['month', 'day', 'hour']
            if not any(field in data.get('group_type') for field in group_type_field):
                return False

            return True
        except json.JSONDecodeError:
            return False
