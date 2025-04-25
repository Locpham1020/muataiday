from flask import Blueprint, request, jsonify

click_bp = Blueprint("click", __name__)

@click_bp.route("/", methods=["POST"])
def log_click():
    data = request.get_json()
    return jsonify({
        "status": "success",
        "data": data
    })
