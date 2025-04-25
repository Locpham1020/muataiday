from flask import Blueprint, request, jsonify
from utils.airtable import send_to_airtable
from config import AIRTABLE_TOKEN, AIRTABLE_BASE_ID

click_bp = Blueprint("click", __name__)
TABLE_NAME = "Goiphubac"  # Tên bảng thật trong Airtable

@click_bp.route("/", methods=["POST"])
def log_click():
    try:
        data = request.get_json()
        response = send_to_airtable(
            token=AIRTABLE_TOKEN,
            base_id=AIRTABLE_BASE_ID,
            table_name=TABLE_NAME,
            payload={"fields": data}
        )
        return jsonify({"status": "success", "data": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
