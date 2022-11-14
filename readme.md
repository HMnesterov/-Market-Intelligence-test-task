# Тестовое задание для стажера в Market Intelligence.

## Запуск:

1)git clone https://github.com/BenitoSwaggolini/-Market-Intelligence-test-task.git

2)pip install -r requirements.txt

3)redis-server

4)uvicorn main:app --host 0.0.0.0 --port 8000 --reload


##Через Docker:
1)git clone https://github.com/BenitoSwaggolini/-Market-Intelligence-test-task.git

2)docker-compose up -d


## API:

127.0.0.1:8000/generate?text='Ваше сообщение'&secret-phrase='Ваша секретная фраза' - отдаёт назад в Json секретный ключ

127.0.0.1:8000/secrets/{secret_key(с метода generate)}?secret-phrase='Секретная фраза' 


## Задача:

Нужно сделать HTTP сервис для одноразовых секретов наподобие [https://onetimesecret.com/](https://onetimesecret.com/?locale=ru).

Он должен позволить создать секрет, задать кодовую фразу для его открытия и cгенерировать код, по которому можно прочитать секрет только один раз. UI не нужен, это должен быть JSON Api сервис.

Для написание сервиса можно использовать [FastAPI](https://github.com/tiangolo/fastapi) или любой другой фреймворк.

- Метод `/generate` должен принимать секрет и кодовую фразу и отдавать `secret_key` по которому этот секрет можно получить.
- Метод `/secrets/{secret_key}` принимает на вход кодовую фразу и отдает секрет.

### Требования:

- Язык программирования: Python 3.7.
- Использование [Docker](https://www.docker.com), сервис должен запускаться с помощью [`docker-compose up`](https://docs.docker.com/compose/reference/up/).
- Требований к используемым технологиям нет.
- Код должен соответствовать PEP, необходимо использование type hints, к публичным методам должна быть написана документация на английском языке.

### Усложнения:

- Написаны тесты (постарайтесь достичь покрытия в 70% и больше). Вы можете использовать [pytest](https://docs.pytest.org/en/latest/) или любую другую библиотеку для тестирования.
- Сервис асинхронно обрабатывает запросы.
- Данные сервиса хранятся во внешнем хранилище, запуск которого также описан в `docker-compose`. Мы рекомендуем использовать [MongoDB](https://www.mongodb.com), но Вы можете использовать любую подходящую базу.
- Секреты и кодовые фразы не хранятся в базе в открытом виде.
- Добавлена возможность задавать время жизни для секретов. Можно попробовать реализовать это с помощью [TTL индексов](https://docs.mongodb.com/manual/core/index-ttl/).
