import os
from datetime import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from habit.services import format_date_time

from dotenv import load_dotenv

load_dotenv()

class HabitMixin(APITestCase):
    reg_url = 'http://127.0.0.1:8000/user/register/'
    token_url = 'http://127.0.0.1:8000/user/token/'
    user_data = {
        'email': 'test@example.com',
        'password': 'testpassword',
    }

    def _register_user(self):
        self.client.post(self.reg_url, self.user_data, format='json')

    def get_headers(self):
        headers = {}
        self._register_user()

        respounse = self.client.post(
            self.token_url, self.user_data, format='json'
        )
        token = 'Bearer ' + respounse.data.get('access')
        headers['Authorization'] = token

        return headers


class HabitAPITest(HabitMixin, APITestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/habit/'
        self.headers = self.get_headers()
        self.valid_data = {
            "location": "Location",
            "time": "10:40",
            "action": "Action",
            "nice_habit": True,
            "period": 1,
            "work_time": 5,
            "public": True
        }
        self.invalid_data = {
            "location": "Location",
            "time": "10:40",
            "action": "Action",
            "nice_habit": False,
            "period": 1,
            "public": True,
        }

    def test_habit_create(self):
        create_url = self.url + 'create/'
        respounse = self.client.post(
            create_url,
            headers=self.headers,
            data=self.valid_data,
            format='json'
        )
        self.assertEqual(respounse.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(action='Action').exists())
        self.assertEqual(Habit.objects.get(action='Action').owner.email, self.user_data.get('email'))

    def test_habit_list(self):
        self.test_habit_create()

        respounse = self.client.get(
            self.url, headers=self.headers, format='json'
        )
        self.assertIn('results', respounse.data)

    def test_habit_public_list(self):
        habit_public = Habit.objects.create(**self.valid_data)
        habit_public.save()

        self.valid_data['public'] = False
        self.valid_data['action'] = 'Public False'

        habit_unpublic = Habit.objects.create(**self.valid_data)
        habit_unpublic.save()

        respounse = self.client.get(
            self.url + 'public/', headers=self.headers
        ).json()

        habit = Habit.objects.get(action='Action')
        self.assertEqual(habit.action, respounse.get('results')[0].get('action'))

    def test_habit_destroy(self):
        self.test_habit_create()

        respounse = self.client.delete(self.url + 'delete/2/', headers=self.headers)
        self.assertEqual(respounse.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_update(self):
        self.test_habit_create()
        self.valid_data['action'] = "test patch"
        respounse = self.client.patch(self.url + 'update/6/', data=self.valid_data, headers=self.headers)

        self.assertEqual(respounse.status_code, status.HTTP_200_OK)

        self.assertEqual(Habit.objects.get(pk=6).action, "test patch")

class FormatDateTimeTestCase(TestCase):
    def test_format_date_time(self):
        time = "10:30"

        current_datetime = datetime.now()

        expected_formatted_time = current_datetime.replace(
            hour=10, minute=30, second=0, microsecond=0
        ).strftime('%Y-%m-%d %H:%M')

        formatted_time = format_date_time(time)

        self.assertEqual(formatted_time, expected_formatted_time)
