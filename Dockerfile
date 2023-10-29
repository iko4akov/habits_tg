FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    postgresql \
    redis-server

# Копируем код приложения в контейнер
COPY . /app

# Устанавливаем зависимости для Django
RUN pip3 install django

# Определите рабочую директорию
WORKDIR /app

# Создаем базу данных PostgreSQL и настраиваем ее
RUN service postgresql start && \
    su - postgres -c "createuser myuser -s" && \
    su - postgres -c "createdb mydb"

# Запускаем Redis-сервер
CMD ["redis-server"]

# Запускаем Django-сервер
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# Запускаем Celery (если он у вас есть)
CMD ["celery", "worker", "--app=myapp"]
