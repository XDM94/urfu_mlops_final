import os
import pandas as pd
from catboost.datasets import titanic


# Путь к датасетам
DATASETS_PATH = "../datasets"

# Проверяем, существует ли директория DATASETS_PATH
if not os.path.exists(DATASETS_PATH):
    try:
        os.makedirs(DATASETS_PATH)
        print(f"The {DATASETS_PATH} directory was created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")


# Загрузка датасета Titanic
train_df, _ = titanic()
print(train_df.info())

# Сохранение датасета в CSV
try:
    train_df.to_csv('../datasets/dataset_titanic.csv', index=False)
    print("Datasets successfully saved in the directory ../dataset under names dataset_titanic.csv.")
except Exception as e:
    print("An error occurred while saving datasets:", e)