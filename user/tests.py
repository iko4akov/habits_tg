from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User


class UserAPIViewTest(APITestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/user/'
        self.valid_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }

    def test_user_registration_valid_data(self):
        url = self.url + 'register/'
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email='test@example.com')
        self.assertIsNotNone(user)

    def test_user_registration_invalid_data(self):
        invalid_data = {
            'email': '',
            'password': 'testpassword',
        }
        url = self.url + 'register/'
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email='')

    def test_token_obtain_pair(self):
        self.test_user_registration_valid_data()
        token_url = self.url + 'token/'

        response = self.client.post(token_url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_list(self):
        self.valid_data['is_superuser'] = True
        self.test_user_registration_valid_data()

        token_url = self.url + 'token/'
        response = self.client.post(token_url, self.valid_data, format='json')
        token = 'Bearer ' + response.data.get('access')

        headers = {
            'Authorization': token
        }

        response = self.client.get(self.url, headers=headers, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


from django.core import management
from django.test import TestCase
from user.models import User

class CreateSuperUserCommandTest(TestCase):
    def test_create_superuser(self):
        management.call_command('csu')

        super_user = User.objects.get(email='admin@admin.com')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
