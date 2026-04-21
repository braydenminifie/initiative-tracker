from flask import Blueprint, jsonify, request
from ..services.encounter_service import create_combatant

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