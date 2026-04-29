from flask import Flask, request, jsonify
from predict import predict_category

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    complaint = data.get("complaint", "")

    category = predict_category(complaint)

    return jsonify({
        "category": category
    })

if __name__ == "__main__":
    app.run(port=5000)