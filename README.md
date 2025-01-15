## Установка локально c Docker

1. Склонировать репозиторий:
   ```bash
   git clone https://github.com/Klaxer77/Uralpromcenter.git
2. Создать образы
   ```bash
   docker-compose -f docker-compose.dev.yml build
3. Запустить проект
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
Документация: 
```bash
http://localhost:8000/docs#/

