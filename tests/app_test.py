import sys
import os
from fastapi.testclient import TestClient
from app_test import app

# Устанавливаем правильные пути
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))  # Каталог со скриптами
PROJECT_PATH = os.path.dirname(SCRIPTS_PATH)               # Каталог проекта
SRC_PATH = os.path.join(PROJECT_PATH, 'src')               # Путь к директории src
sys.path.append(SRC_PATH)

print(sys.path)

# Инициализация TestClient с приложением
client = TestClient(app)

def test_api_app():
    # Отправка POST-запроса к эндпоинту /predict/
    response = client.post("/predict/", json={
        "Pclass": 1, "Sex": 0, "Age": 20.0, "SibSp": 0, "Parch": 0, "Fare": 15, "Embarked": 0
    })

    # Парсинг JSON-данных из ответа
    json_data = response.json()
    
    # Проверка, что статус код ответа 200
    assert response.status_code == 200

    # Проверка, что ключ 'survival_prediction' присутствует в JSON-ответе
    assert 'survival_prediction' in json_data, "'survival_prediction' отсутствует в JSON-ответе"
