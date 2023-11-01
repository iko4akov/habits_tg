FROM python:3.11

WORKDIR /code

COPY ./requirements.txt .

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
