from flask import Flask, request, jsonify
from flask_cors import CORS
from models import write_data, export_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Tracking API for muataiday.store is running.'

@app.route("/api/<base>/<table>", methods=["POST"])
def log_data(base, table):
    try:
        data = request.get_json()
        write_data(base, table, data)
        return jsonify({"status": "success", "data": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/<base>/<table>", methods=["GET"])
def get_data(base, table):
    try:
        data = export_data(base, table)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
