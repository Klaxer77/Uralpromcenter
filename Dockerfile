FROM python:3.10

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY req.txt .

RUN pip install --upgrade pip --no-cache-dir -i https://pypi.org/simple
RUN pip install -r req.txt --no-cache-dir -i https://pypi.org/simple


COPY . .