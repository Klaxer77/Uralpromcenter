FROM python:3.10-bullseye

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt .

RUN python -m pip install -r req.txt --no-cache-dir --no-compile

COPY . .