# Aviator

## Description

A Django website to top up your balance with a tech support chat on websockets.

## Tech

Django, daphne, nginx, redis, PostgreSQL

## How to launch

Create an .env file in the root of the project of the form:

```env
EMAIL_HOST_USER = <your email for sending notifications to users>
EMAIL_HOST_PASSWORD = <email password>
SECRET_KEY = <your secret key>
REDIS_PORT=<redis port>
REDIS_HOST=<redis host>
```

From the root directory, run docker-compose

```bash
docker-compose up -d
```

At the first launch, you need to create an admin, go to the container and do it

```bash
docker exec -it aviator-web-1 bash
cd app
python manage.py createsuperuser
```

The admin panel will be available at http://0.0.0.0/admin , the site itself - http://0.0.0.0/

## Screenshots

*Authorization Page*
![Снимок экрана от 2023-06-22 11-28-21](https://github.com/komediantto/Aviator/assets/62796239/afd7e435-f3f1-44f5-9e52-6c69d46d63b9)

*Home Page*
![Снимок экрана от 2023-06-22 11-29-37](https://github.com/komediantto/Aviator/assets/62796239/bd5fd36d-c46f-4a00-8a5a-87997deeacfd)

*Chat Page*
![Снимок экрана от 2023-06-22 11-30-17](https://github.com/komediantto/Aviator/assets/62796239/5e7e7899-84aa-4877-bb94-160c30636265)

*Admin panel*
![Снимок экрана от 2023-06-22 11-30-27](https://github.com/komediantto/Aviator/assets/62796239/48303bdf-4ca8-4bd6-8c2a-10b532dd9f57)

