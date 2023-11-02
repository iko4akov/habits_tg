FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential libpq-dev && apt-get clean

RUN adduser -rms /bin/bash userapp && chmod 777 /opt /run

WORKDIR .

COPY --chown=userapp:userapp . .

RUN pip install -r requirements.txt

USER userapp
