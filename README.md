путь к venv 
PS1="\u@\h:\w$ "
для генерации secret key
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
celery -A config beat -l info -S django
celery -A config worker -l info -S django
redis-server
