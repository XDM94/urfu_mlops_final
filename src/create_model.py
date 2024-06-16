import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, r2_score
import pickle


# Получаем правильные пути
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))      # Каталог со скриптами
PROJECT_PATH = os.path.dirname(SCRIPTS_PATH)                   # Каталог проек
# Пути к датасетам и моделям
DATASETS_PATH = PROJECT_PATH + "/datasets/"

# Загрузка датасета Titanic из файла CSV
train_df = pd.read_csv(DATASETS_PATH + 'dataset_titanic.csv')

# Заполнение пропущенных значений
train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
train_df['Embarked'] = train_df['Embarked'].fillna(train_df['Embarked'].mode()[0])

# Преобразование категориальных признаков
label_encoders = {}
for col in ['Sex', 'Embarked']:
    le = LabelEncoder()
    train_df[col] = le.fit_transform(train_df[col])
    label_encoders[col] = le

# Разделение данных на признаки и целевую переменную
X = train_df.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y = train_df['Survived']

# Разделение на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели случайного леса
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Предсказание на тестовом наборе
y_pred = rf_model.predict(X_test)

# Оценка качества модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
r2 = r2_score(y_test, y_pred)
print(f"Сoefficient of determination: {r2}")

print('Classification Report:')
print(classification_report(y_test, y_pred))

# Проверяем, существует ли директория DATASETS_PATH
model_path = os.path.join(PROJECT_PATH, "models")
if not os.path.exists(model_path):
    try:
        os.makedirs(model_path)
        print(f"The {model_path} directory was created successfully.")
    except OSError as e:
        print(f"Error creating directory: {e}")

# Сохраняем модель
model_path = os.path.join(model_path, 'model_titanic.pkl')
with open(model_path, 'wb') as file:
    pickle.dump(rf_model, file)
    print('The model was saved successfully: ../models/model_titanic.pkl')