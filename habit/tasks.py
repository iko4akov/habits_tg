import json
from datetime import datetime, timedelta
import os

import requests
from dotenv import load_dotenv


from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule


load_dotenv()

@shared_task
def set_schedule(**data):
    schedule, create = IntervalSchedule.objects.get_or_create(
        every="1",
        period=IntervalSchedule.DAYS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name='qq',
        task='habit.tasks.send_habit',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps(
            data
        ),
        expires=datetime.utcnow() + timedelta(seconds=30),
        start_time=data.get('time')
        )

@shared_task()
def send_habit(data):
    print(data)
    bot_token = os.getenv('BOT_TOKEN')
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    message_text = f'Я буду {data.get("action")} столько {data.get("work_time")} мин в {data.get("location")} ' \
                   f'{data.get("tg")}'
    params = {
        'chat_id': data.get('tg'),
        'text': message_text
    }
    response = requests.post(url, params=params)

    if response.status_code == 200:
        print('Сообщение успешно отправлено!')
    else:
        print('Произошла ошибка при отправке сообщения.')
        print(response.text)
