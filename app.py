import os
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/match", methods=["POST"])
def match_degree():
    req = request.get_json()
    degree_input = req.get("degree", "").strip()
    careers = []
    for key, value in data.items():
        if key.lower() == degree_input.lower():
            careers = value.get("careers", [])
            break
    return jsonify({"careers": careers})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)

