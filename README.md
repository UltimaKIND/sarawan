# Магазин продуктов "Сарафан"

## Tech Stack

- django rest framework
- postgresql


## Запуск

- перед запуском указать параметры подключения к бд в файле .env

клонировать репозиторий

```sh
git clone git@github.com:UltimaKIND/sarawan.git
```

перейти в папку с проектом

```sh
  cd sarawan
```

установить зависимости

```sh
  poetry install
```

активировать виртуальное окружение

```sh
  poetry shell
```

накатить миграции на базу данных

```sh
  python3 manage.py migrate
```

наполнить бд данными

```sh
  python3 manage.py fill
```

запустить сервер

```sh
  python3 manage.py runserver
```