from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model at the top-level to ensure it is loaded when the script is executed
model_path = 'gbm_pipeline.pkl'  # Update this path if the model is not in the same directory as this script
model = None

try:
    model = joblib.load(model_path)
    print("Model loaded successfully")
except Exception as e:
    print(f"Failed to load model '{model_path}': {e}")

@app.route('/predict', methods=['POST'])
def predict():
    global model  # Referencing the global model variable
    
    if not model:
        print("Model is not loaded")
        return jsonify({"error": "Model is not loaded"}), 500

    file = request.files.get('file')
    if not file:
        print("No file part in the request")
        return jsonify({"error": "No file part in the request"}), 400

    try:
        test_data = pd.read_csv(file)
        print("File read successfully")
        # Ensure the model is correctly used for predictions
        predictions = model.predict(test_data.drop(columns=['label'], errors='ignore'))
        return jsonify(predictions.tolist())
    except Exception as e:
        print(f"Error processing file: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
