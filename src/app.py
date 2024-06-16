import os
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np
import pandas as pd


# Получаем правильные пути
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))      # Каталог со скриптами
PROJECT_PATH = os.path.dirname(SCRIPTS_PATH)                   # Каталог проекта

# Загрузим модель из файла pickle
model_path = os.path.join(PROJECT_PATH, 'models', 'model_titanic.pkl')
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
    print("The model has been successfully loaded.")

# Определение класса для данных о пассажире
class Passenger(BaseModel):
    Pclass: int         # Класс: 1, 2, 3
#    Sex: str            # Пол: male, female
    Sex: float          # Пол: 0, 1
    Age: float          # Возраст
    SibSp: int          # Количество родственников (супруг+братья\сестры): 0, 1, 2, 3
    Parch: int          # Количество родственников (родители+дети): 0, 1, 2
    Fare: float         # Cтоимость билета
    Embarked: float     # Порт отправления


app = FastAPI()

@app.post("/predict")
async def predict_survival(passenger: Passenger):
    test_data = np.array([[passenger.Pclass, passenger.Sex, passenger.Age,
                       passenger.SibSp, passenger.Parch, passenger.Fare, passenger.Embarked]])

    # Set feature names for RandomForestClassifier
    column_names = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X_test = pd.DataFrame(test_data, columns=column_names)

    prediction = model.predict(X_test)

    return {"survival_prediction": int(prediction[0])}

# Запуск FastAPI приложения
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8091)