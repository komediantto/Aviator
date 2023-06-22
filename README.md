# Aviator

## Описание

Сайт на Django для пополнения баланса с чатом техподдержки на вебсокетах.

## Технологии

Django, daphne, nginx, redis, PostgreSQL

## Как запустить

Создать .env файл в корне проекта вида:

```env
EMAIL_HOST_USER = <ваш email для отправки уведомлений юзерам>
EMAIL_HOST_PASSWORD = <пароль от email>
SECRET_KEY = <ваш secret key>
REDIS_PORT=<redis порт>
REDIS_HOST=<redis хост>
```

Из корневой директории запустить docker-compose

```bash
docker-compose up -d
```

При первом запуске требуется создать админа, идём в контейнер и делаем это

```bash
docker exec -it aviator-web-1 bash
cd app
python manage.py createsuperuser
```

Админка будет доступна по адресу http://0.0.0.0/admin, сам сайт - http://0.0.0.0/

## Скриншоты

*Страница авторизации*
![Снимок экрана от 2023-06-22 11-28-21](https://github.com/komediantto/Aviator/assets/62796239/afd7e435-f3f1-44f5-9e52-6c69d46d63b9)

*Главная страница*
![Снимок экрана от 2023-06-22 11-29-37](https://github.com/komediantto/Aviator/assets/62796239/bd5fd36d-c46f-4a00-8a5a-87997deeacfd)

*Страница чата*
![Снимок экрана от 2023-06-22 11-30-17](https://github.com/komediantto/Aviator/assets/62796239/5e7e7899-84aa-4877-bb94-160c30636265)

*Админка*
![Снимок экрана от 2023-06-22 11-30-27](https://github.com/komediantto/Aviator/assets/62796239/48303bdf-4ca8-4bd6-8c2a-10b532dd9f57)

