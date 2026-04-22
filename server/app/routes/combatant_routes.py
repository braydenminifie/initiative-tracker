from flask import Blueprint, jsonify, request
from ..services.encounter_service import create_combatant, get_combatant, remove_combatant, set_combatant_health
from ..services.condition_service import apply_condition, get_combatant_conditions_by_combatant_id

combatant_bp = Blueprint("combatants", __name__)

@combatant_bp.route("", methods=["POST"])
def create_combatant_route():
    data = request.get_json()

    combatant = create_combatant(
        encounter_id=data["encounter_id"],
        name=data["name"],
        type=data["type"],
        initiative=data["initiative"],
        max_hp = data["max_hp"],
        armour_class = data["armour_class"]
    )

    return jsonify({
        "id": combatant.id,
        "name": combatant.name
    }), 201



@combatant_bp.route("/<int:id>", methods=["GET"])
def get_combatant_route(id):
    combatant = get_combatant(id)

    if not combatant:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": combatant.id,
        "name": combatant.name,
        "type": combatant.type,
        "initiative": combatant.initiative,
        "max_hp": combatant.max_hp,
        "armour_class": combatant.armour_class,
        "encounter_id": combatant.encounter_id
    }), 200



@combatant_bp.route("/<int:id>", methods=["DELETE"])
def delete_combatant_route(id):
    combatant = remove_combatant(id)

    if not combatant:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "message": "Combatant deleted",
        "id": id
    }), 200



@combatant_bp.route("/<int:id>/health", methods=["PATCH"])
def update_health_route(id):
    data = request.get_json()
    health = data.get("health")

    combatant = set_combatant_health(id, health)

    if not combatant:
        return jsonify({"error": "Combatant not found"}), 404

    return jsonify({
        "id": combatant.id,
        "name": combatant.name,
        "hp": combatant.current_hp
    })



@combatant_bp.route("/<int:combatant_id>/apply-condition", methods=["POST"])
def apply_condition_route(combatant_id):
    data = request.get_json()

    combatant_condition = apply_condition(
        combatant_id=combatant_id,
        condition_id=data["condition_id"],
        current_round=data["current_round"],
        current_turn=data["current_turn"],
        duration_turns=data["duration"]
    )

    return jsonify({
        "id": combatant_condition.id,
        "combatant_id": combatant_condition.combatant_id,
        "condition_id": combatant_condition.condition_id
    }), 201

@combatant_bp.route("/<int:combatant_id>/conditions", methods=["GET"])
def get_conditions_route(combatant_id):
    conditions = get_combatant_conditions_by_combatant_id(combatant_id)
    print(conditions)
    print(conditions[0].condition)

    if conditions is None:
        return jsonify({"error": "Combatant not found"}), 404

    return jsonify({
        "combatant_id": combatant_id,
        "conditions": [
            {
                "id": cc.id,
                "name": cc.condition.name,
                "description": cc.condition.description,
                "duration": cc.duration_turns
            }
            for cc in conditions
        ]
    })