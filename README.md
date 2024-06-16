# Настройка переменных окружения

Для Windows:
$env:FLASK_APP = "manage.py"
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = 1

Для Unix/Linux, macOS:
export FLASK_APP=manage.py
export FLASK_ENV=development
export FLASK_DEBUG=1


# Запуск docker-compose.yml
docker-compose up -d

# Миграции базы данных
#### Создание миграций:
flask db migrate -m "Initial migration."

#### Применение миграций:
flask db upgrade

# Запуск приложения
flask run


# Структура проекта

dl/
│
├── venv/  # Виртуальная среда
├── app/
│   ├── __init__.py # Инициализация приложения
│   ├── settings.py  # Основной файл приложения
│   └── database # Все файлы имеющие отношение к бд
│       └── models # Модели Базы данных приложения
├── migrations/  # Директория миграций Alembic
├── requirements.txt  # Зависимости проекта
├── README.md  # Документация проекта
└── manage.py  # Точка входа для командной строки