from ..extensions import db

class CombatantCondition(db.Model):
    __tablename__ = "combatant_conditions"

    id = db.Column(db.Integer, primary_key=True)

    combatant_id = db.Column(db.Integer, db.ForeignKey("combatants.id"), nullable=False)
    condition_id = db.Column(db.Integer, db.ForeignKey("conditions.id"), nullable=False)

    duration_turns = db.Column(db.Integer, nullable=True)

    applied_round = db.Column(db.Integer, nullable=False)
    applied_turn = db.Column(db.Integer, nullable=False)
    applied_total_turn = db.Column(db.Integer, nullable=False)

    is_active = db.Column(db.Boolean, default=True)

    condition = db.relationship("Condition")