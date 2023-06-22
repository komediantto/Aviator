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
![[Снимок экрана от 2023-06-22 11-28-21.png]]

*Главная страница*
![[Снимок экрана от 2023-06-22 11-29-37.png]]

*Страница чата*
![[Снимок экрана от 2023-06-22 11-30-17.png]]

*Админка*
![[Снимок экрана от 2023-06-22 11-30-27.png]]
