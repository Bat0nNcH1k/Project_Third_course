import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

print("→ Загружаем датасет...")

csv_path = 'backend/dataset.csv'

df = pd.read_csv(csv_path)

if 'phishing' not in df.columns:
    raise ValueError("В CSV должен быть столбец 'phishing' с метками классов.")

X = df.drop(columns=['phishing'])
y = df['phishing']

print(f"→ Всего признаков: {X.shape[1]}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("→ Обучаем модель...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open("backend/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("backend/features.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("✅ Модель успешно обучена и сохранена как model.pkl и features.pkl.")
