from flask import Blueprint, request, jsonify
from .services import create_package, get_package, update_status, update_location

bp = Blueprint('routes', __name__)

@bp.route('/packages', methods=['POST'])
def create():
           data = request.json
           return jsonify(create_package(data)), 201

@bp.route('/packages/<int:package_id>', methods=['GET'])
def get(package_id):
        package = get_package(package_id)
        if not package:
                return jsonify({"error" : "Not Found"}), 404
        return jsonify(package)

@bp.route("/packages/<int:package_id>/status", methods=['PUT'])
def update(package_id):
        data = request.json
        result = update_status(package_id, data.get("status"))

        if "error" in result:
                return jsonify(result), 400
        
        return jsonify(result)