# Check producer

## Описание проекта

Сервис отвечает за прием, валидацию и запись чеков в журнал, а также их передачу сервису аналитики.

## Технологии

- Linux
- Python
- pip+venv
- Django
- DRF
- PostgreSQL
- Docker
- Docker Compose (итоговая сборка)

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле requirements.txt.
Чтобы установить зависимости, используйте команду `pip install -r requirements.txt`

## Документация

Документация находится по ссылкам:
1. Swagger `api/schema/swagger-ui/`

## Тестовый пользователь

`username: User_producer`

`password: producer`

## Как запустить проект

Проект запускается с помощью Docker-compose совместно с приложением `check_consumer`. Инструкцию по запуску смотрите в README-файле репозитория `https://github.com/UlianaSem/check_project`.

## Файл .env.example

1. Данные для БД
   1. Название БД `DATABASES_NAME` 
   2. Имя пользователя `POSTGRES_USER`
   3. Пароль `POSTGRES_PASSWORD`
   4. Хост `DATABASES_HOST` (как указан Docker-compose)
2. Данные для Kafka 
   1. Хост `KAFKA_HOST` (как указан Docker-compose)
   2. Клиент `KAFKA_CLIENT`
   3. Порт `KAFKA_PORT`
3. Настройки Django `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/