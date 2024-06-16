import sys
import os
# Получаем правильные пути
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))      # Каталог со скриптами
PROJECT_PATH = os.path.dirname(SCRIPTS_PATH)                   # Каталог проекта
src_path = os.path.join(PROJECT_PATH, 'src')
sys.path.append(src_path)
print(sys.path)

from fastapi.testclient import TestClient
from app_test import app


client = TestClient(app)
def test_api_app():
    response = client.post("/predict/",
                           json={"Pclass": 1, "Sex": 0, "Age": 20.0, "SibSp": 0, "Parch": 0, "Fare": 15, "Embarked": 0})
    json_data = response.json()
    assert response.status_code == 200

    # Проверяем, что ключ 'survival_prediction' присутствует в словаре json_data
    assert 'survival_prediction' in json_data, "'survival_prediction' field missing in JSON response"