from flask import Flask, jsonify, request
from app_logic import add_numbers

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(message="Hello, world!"), 200

    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok"), 200

    @app.post("/adds")
    def add():
        data = request.get_json(silent=True) or {}
        a = data.get("a")
        b = data.get("b")
        try:
            result = add_numbers(a, b)
        except (TypeError, ValueError) as e:
            return jsonify(error=str(e)), 400
        return jsonify(result=result), 200

    return app

# For `flask run` convenience
app = create_app()
