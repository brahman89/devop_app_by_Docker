FROM python:3.9-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry==1.4.2

# Отключаем создание виртуального окружения внутри Poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости
RUN poetry install --no-dev --no-interaction --no-ansi

# Копируем код приложения
COPY . /app

# Собираем статику
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]