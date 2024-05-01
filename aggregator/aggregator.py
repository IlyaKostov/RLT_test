from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class PaymentAggregator:
    def __init__(self, data: dict[str]):
        self.dt_from = data.get('dt_from')
        self.dt_upto = data.get('dt_upto')
        self.group_type = data.get('group_type')
        self.dt_from_iso = datetime.fromisoformat(self.dt_from)
        self.dt_upto_iso = datetime.fromisoformat(self.dt_upto)
        self.group_format = {
            'month': '%Y-%m-01T00:00:00',
            'day': '%Y-%m-%dT00:00:00',
            'hour': '%Y-%m-%dT%H:00:00'
        }

    async def aggregate_data(self, db):

        group_id = {'$dateToString': {'format': self.group_format.get(self.group_type, ''), 'date': '$dt'}}

        pipeline = [
            {'$match': {'dt': {'$gte': self.dt_from_iso, '$lte': self.dt_upto_iso}}},
            {'$group': {'_id': group_id, 'total_value': {'$sum': '$value'}}},
            {'$sort': {'_id': 1}},
        ]

        result_list = await db.aggregator(pipeline)

        dataset, labels = await self.fill_missing_dates(result_list)

        response = {'dataset': dataset, 'labels': labels}
        return response

    async def fill_missing_dates(self, data_list: list[dict[str]]):
        start_date = self.dt_from_iso
        end_date = self.dt_upto_iso

        date_total_map = {d['_id']: d['total_value'] for d in data_list}

        dataset = []
        labels = []
        current_date = start_date
        while current_date <= end_date:
            current_date_str = current_date.strftime(self.group_format.get(self.group_type, ''))
            labels.append(current_date_str)
            dataset.append(date_total_map.get(current_date_str, 0))

            if self.group_type == 'month':
                current_date += relativedelta(months=1)
            elif self.group_type == 'day':
                current_date += timedelta(days=1)
            elif self.group_type == 'hour':
                current_date += timedelta(hours=1)

        return dataset, labels
