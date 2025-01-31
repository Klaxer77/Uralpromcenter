FROM python:3.10-bullseye

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt .

RUN pip install --upgrade pip

RUN pip install -r req.txt

COPY . .