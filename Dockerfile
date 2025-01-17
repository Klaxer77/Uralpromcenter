FROM python:3.10

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt .

RUN python -m pip install --upgrade pip

RUN python -m pip install --no-cache-dir -r req.txt

COPY . .