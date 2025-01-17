FROM python:3.10

# Создаем директорию приложения
RUN mkdir /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем файл зависимостей
COPY req.txt .

# Устанавливаем более старую версию pip (при необходимости)
RUN pip install pip==20.2.4  # Замените на желаемую версию по необходимости

# Обновляем pip с небольшой задержкой для избежания ошибок
RUN sleep 5 && pip install --upgrade pip

# Устанавливаем зависимости из файла
RUN pip install -r req.txt

# Копируем исходный код приложения
COPY . .
