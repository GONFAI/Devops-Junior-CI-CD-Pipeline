import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "DevOps Junior App")
    env = os.getenv("ENV", "local")

    logging.info("Home endpoint called")

    return jsonify(
        app=app_name,
        environment=env,
        message="DevOps Junior CI/CD Pipeline Running 🚀"
    )

@app.route("/health")
def health():
    return jsonify(status="OK")

@app.route("/ready")
def ready():
    return jsonify(status="READY")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

