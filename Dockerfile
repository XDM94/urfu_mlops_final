# Используем официальный образ Python
FROM python:3.10-slim

# Обновляем список пакетов и устанавливаем curl
#RUN apt-get update && apt-get install -y curl

# Устанавливаем рабочий каталог приложения в контейнере
WORKDIR /usr/src/app

# Копируем файл requirements.txt в каталог нашего приложения
COPY requirements.txt ./

# Устанавливаем необходимые модули для Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения в контейнер
COPY . .

# Запускаем приложение
CMD ["uvicorn", "src.api_app_titanic:app", "--host", "0.0.0.0", "--port", "8091"]