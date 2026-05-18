from flask import Blueprint, jsonify, request
from ..models.encounter import Encounter
from ..extensions import db
from ..services.encounter_service import create_encounter, get_encounter, get_encounter_state, get_all_encounters
from ..services.combat_engine import next_turn

encounter_bp = Blueprint("encounters", __name__)



@encounter_bp.route("/", methods=["GET"])
def get_all_encounters_route():
    encounters = get_all_encounters()

    return jsonify([
        {
            "id": encounter.id,
            "name": encounter.name,
            "round": encounter.current_round,
            "turn": encounter.total_turns_elapsed
        }
        for encounter in encounters
    ]), 200



@encounter_bp.route("", methods=["POST"])
def create_encounter_route():
    data = request.get_json()

    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    encounter = create_encounter(name)

    return jsonify({
        "id": encounter.id,
        "name": encounter.name,
        "round": encounter.current_round
    }), 201



@encounter_bp.route("/<int:id>/next-turn", methods=["POST"])
def next_turn_route(id):
    encounter = get_encounter(id)

    if not encounter:
        return jsonify({"error": "Not found"}), 404

    result = next_turn(encounter)

    return jsonify(result)



@encounter_bp.route("/<int:id>/state", methods=["GET"])
def get_encounter_state_route(id):
    state = get_encounter_state(id)

    if not state:
        return jsonify({"error": "Encounter not found"}), 404

    return jsonify(state)