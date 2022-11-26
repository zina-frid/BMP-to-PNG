# Базовый образ
FROM python:3.9 AS builder
COPY requirements.txt .

# Установка зависимостей
RUN pip install --user -r requirements.txt

# Новый минималистичный образ
FROM python:3.9-slim
WORKDIR /code

# Копируем зависимости и код в новый образ
COPY --from=builder /root/.local /root/.local
COPY . .

# Задаём переменную окружения
ENV PATH=/root/.local:$PATH

# Задаём команду исполнения
CMD ["python", "-u", "./main.py"]
