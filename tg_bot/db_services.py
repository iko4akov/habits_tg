import os
import requests
from dotenv import load_dotenv

class HandlerAPIRequests:
    load_dotenv()
    url = os.getenv('HOST_APP')+os.getenv('PORT_APP')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.example.com/page1',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': '*/*',
    }

    def __init__(self, data: dict = None):
        self.data = data
        self._get_admin_token()

    def create_user(self):
        create_url = self.url + 'user/register/'
        try:
            respounse = requests.post(create_url, data=self.data, headers=self.headers)
            return respounse.status_code == 201

        except Exception:
            return False

    def _get_admin_token(self) -> None:
        token_url = self.url + 'user/token/'
        data = {}
        data['email'] = 'admin@admin.com'
        data['password'] = os.getenv('PASSWORD_SU')
        respounse = requests.post(token_url, data).json()
        access = respounse.get('access')
        token = 'Bearer ' + access
        self.headers['Authorization'] = token

    def _get_user_id_db(self):
        """Получение айди пользователя в приложении по его айди в телеграм"""
        telegram_id = self.data.get('telegram_id')
        get_id_url = self.url + f'user/?telegram_id={telegram_id}'
        respounse = requests.get(get_id_url).json()
        if respounse:
            return respounse['id']

    def habit_list_owner(self):
        url_list = self.url + f'habit/?owner={self._get_user_id_db()}'
        respounse = requests.get(url_list, headers=self.headers).json()
        return respounse.get('results')

    def habit_list_public(self):
        url_list = self.url + 'habit/public/'
        respounse = requests.get(url_list, headers=self.headers).json()
        print(respounse.get('results'))
        return respounse.get('results')
