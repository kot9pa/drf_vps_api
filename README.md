# REST-сервис для управления виртуальными серверами (VPS) с использованием Django Rest Framework (DRF)

## Описание
Объект VPS включают следующие параметры:  
```
uid — уникальный идентификатор сервера.  
cpu — количество процессорных ядер.  
ram — объем оперативной памяти.  
hdd — объем дискового пространства.  
status — текущий статус сервера (например, started, blocked, stopped).
```

API предоставляет следующие возможности:
1. Создание нового виртуального сервера.
2. Получение данных о конкретном сервере по его uid.
3. Вывод списка всех серверов с поддержкой фильтрации по заданным параметрам.
4. Изменение статуса сервера (например, перевод в состояния started, blocked, stopped).

## Старт проекта
Создать `.env`, пример `.env.example`

Установить зависимости:  
`poetry install`

Активировать виртуальное окружения:  
`poetry shell`

Поднять контейнер Postgres:  
`docker-compose up -d`

Создать и накатить миграции:  
`poetry run python manage.py makemigrations`  
`poetry run python manage.py migrate`  
`poetry run python manage.py createcachetable`

Запуск приложения:  
`poetry run python manage.py runserver`

## Документация API
Swagger:  
`http://127.0.0.1:8000/api/swagger/`

Redoc:  
`http://127.0.0.1:8000/api/redoc/`

Администрирование:  
`http://127.0.0.1:8000`