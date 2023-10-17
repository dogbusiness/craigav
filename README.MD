## Classified advertisements website

## Project description

<details>
<summary>English</summary>

## What is this?
Basically this is the clone of Russian Avito / American Craiglist

## Why is it good?
It has minimalistic design, all django features(migrations, admin, auth) and web-server to give static.

## What is under the hood?
The app is written with:
- Backend: Django
- Database: PostgreSQL
- Front: Bootsrap
- Web server: Nginx gives static, solves "leaky bucket" problem
- Containers: Docker compose

## How to install?
```docker compose build && docker compose up -d```


## Disclaimer
The app was originally written in the last year (2022). The current commit is the attempt to refactor code and enhance the app with nginx and psql (previously sqlite)

</details>


<details>
<summary>Russian</summary>

## Что это?
Это простой клон российского Авито / Американского Craiglist

## Почему это хорошо?
У приложения минималистичный дизайн, все фичи джанго (миграции, админка, аутентификация) веб-сервер, отдающий статику

## Что под капотом?
The app is written with:
- Бекэнд Django
- СУБД: PostgreSQL
- Фронт: Bootsrap
- Веб-сервер: Nginx отдает статику, решает проблему "протекающего ведра"
- Containers: Docker compose

## Как установить и запустить?
```docker compose build && docker compose up -d```


## Дисклеймер
Приложение было написано в прошлом году (2022). Текущий коммит - попытка рефакторинга кода и улучшения посредством добавления nginx и замены sqlite на psql.

</details>
