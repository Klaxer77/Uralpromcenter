FROM python:3.10

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt .

RUN python -m pip install --upgrade pip --no-cache-dir
RUN python -m pip install -r req.txt --no-cache-dir

COPY . .