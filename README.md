# Implantum Telegram Bot

Каркас Telegram-бота для стоматологической клиники.

## Возможности каркаса

- запуск на `aiogram 3`;
- команды `/start` и `/help`;
- заготовка сценария записи на приём;
- асинхронное подключение к базе данных;
- настройки из переменных окружения;
- базовая настройка логирования и тестов.

## Быстрый старт

Требуется Python 3.11 или новее.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
```

Укажите токен от `@BotFather` в `.env`, затем запустите:

```bash
python -m bot
```

Проверки проекта:

```bash
pytest
ruff check .
mypy src
```

## Структура

```text
src/bot/
├── config.py       # настройки приложения
├── main.py         # сборка и запуск бота
├── handlers/       # Telegram-команды и сообщения
├── keyboards/      # кнопки и меню
├── services/       # бизнес-логика
└── database/       # подключение к БД и модели
tests/              # автоматические тесты
```

