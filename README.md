# Bot worker 
Репозиторий содержащий worker'а предоставляющего интерфейс для конечного пользователя
## Требования для установки
- `Make` версии 4.4 и выше
- `Python` версии 3.10 и выше
- `Poetry` версии 1.3.1 и выше
- (Опционально)`Docker` версии 20.10.22 и выше
## Подготовка к запуску
### Заполнение .env
Необходимо создать в корневой папке проекта файл `.env` с переменными окружения.
Пример заполнения:
```shell
BOT_TOKEN=token
BACKEND_CLIENT_HOSTNAME=localhost
BACKEND_CLIENT_PORT=8000
BACKEND_CHARACTER_HOSTNAME=localhost
BACKEND_CHARACTER_PORT=8001
```
### Установка зависимостей
Для локального запуска:
```shell
make prepare
```
Для запуска в докере:
```shell
make build
```
## Запуск
### Запуск в докере
```shell
make run-docker
```
### Локальный запуск
```shell
make run
```