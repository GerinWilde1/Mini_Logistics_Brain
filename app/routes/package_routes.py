from flask import Blueprint, request, jsonify
from app.services import package_service

bp = Blueprint("packages", __name__)


#Create
@bp.route("/packages", methods=["POST"])
def create_package():
    data = request.json
    result = package_service.create_package(data)
    return jsonify(result), 201

# Get One
@bp.route("/packages/<package_id>", methods=["GET"])
def get_package(package_id):
    package = package_service.get_package(package_id)

    if not package:
        return jsonify({"error": "Not found"}), 404

    return jsonify(package), 200

# Update Status
@bp.route("/packages/<package_id>/status", methods=["PUT"])
def update_status(package_id):
    data = request.json

    if not data or "status" not in data:
        return jsonify({"error": "Invalid data"}), 400

    result, error = package_service.update_status(package_id, data["status"])

    if error == "not_found":
        return jsonify({"error": "Not found"}), 404

    if error == "invalid_transition":
        return jsonify({"error": "Invalid transition"}), 400

    return jsonify(result), 200

# List + Filter + Pagination
@bp.route("/packages", methods=["GET"])
def list_packages():
    status = request.args.get("status")
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    result = package_service.get_packages(status, page, limit)
    return jsonify(result)

# Count
@bp.route("/packages/count", methods=["GET"])
def get_package_count():
    total = package_service.count_packages()
    return jsonify({"count": total}), 200

#Metrics
@bp.route("/metrics", methods=["GET"])
def get_metrics():
    result = package_service.get_metrics()
    return jsonify(result)
