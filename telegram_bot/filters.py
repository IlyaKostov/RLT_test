import json
from datetime import datetime

from aiogram.filters import Filter
from aiogram.types import Message


class IsFormatFieldsFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        try:
            data = json.loads(message.text)
            if not isinstance(data, dict):
                return False
            print(data)
            required_fields = ['dt_from', 'dt_upto', 'group_type']
            if not all(field in data for field in required_fields):
                return False

            dt_from = data.get('dt_from')
            dt_upto = data.get('dt_upto')
            group_type = data.get('group_type')

            group_type_field1 = ['month', 'day', 'hour']
            if not any(field in group_type for field in group_type_field1):
                return False

            if datetime.fromisoformat(dt_from) >= datetime.fromisoformat(dt_upto):
                return False

            return True

        except json.JSONDecodeError:
            return False
