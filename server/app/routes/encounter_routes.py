from flask import Blueprint, jsonify
from ..models.encounter import Encounter
from ..extensions import db

encounter_bp = Blueprint("encounters", __name__)

@encounter_bp.route("/", methods=["GET"])
def get_encounters():
    encounters = Encounter.query.all()

    return jsonify([
        {
            "id": e.id,
            "name": e.name,
            "round": e.current_round
        }
        for e in encounters
    ])