FROM python:3.9.6-alpine

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN apk add gcc musl-dev g++ zlib-dev jpeg-dev libjpeg postgresql-libs postgresql-dev

RUN pip install pipenv

RUN pipenv install

RUN pip install uvicorn