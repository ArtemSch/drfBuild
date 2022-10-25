FROM python:3.10.0-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django

ENV PROJECT_ROOT=/web_django


RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests default-libmysqlclient-dev -y \
    && pip install --no-cache-dir pipenv gunicorn \
    && apt-get clean \
    && echo Installation finished...


RUN apt install python3-pip -y
WORKDIR $PROJECT_ROOT
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt


ADD . /web_django/
