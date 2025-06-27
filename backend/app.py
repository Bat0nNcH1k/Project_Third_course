from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import feature_extractor

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

@app.route("/")
def index():
    return "Сервер работает!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "URL не передан"}), 400

    try:
        print("→ Извлекаем признаки из URL:", url)
        extracted = feature_extractor.extract_features(url)
        input_df = pd.DataFrame([extracted])[features]
        prediction = model.predict(input_df)[0]
        print("→ Предсказание:", prediction)
        return jsonify({
            "result": "phishing" if prediction == 1 else "legitimate",
            "confidence": 0.5,  # можно улучшить при доработке модели
            "features_used": features
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
