from flask import Blueprint, request, jsonify
from app.services.condition_service import create_condition, apply_condition, get_all_conditions

condition_bp = Blueprint("condition", __name__)


@condition_bp.route("", methods=["POST"])
def create_condition_route():
    data = request.get_json()

    name = data.get("name")
    description = data.get("description")
    is_debuff = data.get("is_debuff")

    
    condition = create_condition(name, description, is_debuff)
    

    return jsonify({
        "id": condition.id,
        "name": condition.name,
        "description": condition.description,
        "is_debuff": condition.is_debuff
    }), 201


@condition_bp.route("/", methods=["GET"])
def get_all_conditions_route():
    conditions = get_all_conditions()

    return jsonify([
        {
            "id": condition.id,
            "name": condition.name,
            "description": condition.description,
            "is_debuff": condition.is_debuff
        }
        for condition in conditions
    ]), 200