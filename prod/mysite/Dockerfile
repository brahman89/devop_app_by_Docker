FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем pipenv
RUN pip install --no-cache-dir pipenv

WORKDIR /app

# Копируем Pipfile и Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Устанавливаем зависимости без создания виртуального окружения
RUN pipenv install --deploy --system --ignore-pipfile

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]