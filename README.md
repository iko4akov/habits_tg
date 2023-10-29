# run peoject for server

1. connect server `$ ssh your_name@server_ip(example: 1.2.3.4)`

2. clone project






путь к venv 
PS1="\u@\h:\w$ "
для генерации secret key
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
celery -A config beat -l info -S django
celery -A config worker -l info -S django
redis-server
coverage run --source='.' manage.py test~~