from flask import Blueprint, jsonify, request
from utils.airtable import get_all_records
from config import AIRTABLE_TOKEN, AIRTABLE_BASE_ID

export_bp = Blueprint("export", __name__)

@export_bp.route("/", methods=["GET"])
def export_data():
    table = request.args.get("table")
    if table not in ["log_click", "log_order"]:
        return jsonify({"error": "Invalid or missing table parameter"}), 400

    try:
        records = get_all_records(
            token=AIRTABLE_TOKEN,
            base_id=AIRTABLE_BASE_ID,
            table_name=table
        )
        return jsonify({"data": records})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
