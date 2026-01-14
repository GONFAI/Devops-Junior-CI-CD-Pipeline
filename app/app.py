import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "DevOps Junior App")
APP_ENV = os.getenv("APP_ENV", "local")

@app.route("/")
def home():
    return jsonify(
        message=f"{APP_NAME} Running 🚀",
        environment=APP_ENV
    )

@app.route("/health")
def health():
    return jsonify(status="OK")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
