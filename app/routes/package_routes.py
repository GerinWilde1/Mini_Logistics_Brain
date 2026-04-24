from flask import Blueprint, request, jsonify
from app.services import package_service

bp = Blueprint("packages", __name__)

@bp.route("/packages", methods=["POST"])
def create():
    data = request.json
    result = package_service.create_package(data)
    return jsonify(result), 201


@bp.route("/packages/<package_id>", methods=["GET"])
def get(package_id):
    package = package_service.get_package(package_id)

    if not package:
        return jsonify({"error": "Not found"}), 404

    return jsonify(package), 200


@bp.route("/packages/<package_id>/status", methods=["PUT"])
def update_status(package_id):
    data = request.json
    result, error = package_service.update_status(package_id, data["status"])

    if error == "not_found":
        return jsonify({"error": "Not found"}), 404

    if error == "invalid_transition":
        return jsonify({"error": "Invalid transition"}), 400
    
    if not data or "location" not in data:
        return jsonify({"error": "Invalid data"}), 400

    return jsonify(result), 200

@bp.route("/packages", methods=["GET"])
def list_packages():
    status = request.args.get("status")
    result = package_service.list_packages(status)
    return jsonify({
    "success": True,
    "count": len(result),
    "data": result
})

@bp.route("/packages/count", methods=["GET"])
def count():
    total = package_service.count_packages()
    return jsonify({"count": total}), 200

@bp.route("/metrics", methods=["GET"])
def metrics():
    result = package_service.get_metrics()
    return jsonify(result), 200