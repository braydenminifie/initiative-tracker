from ..extensions import db

class Encounter(db.Model):
    __tablename__ = "encounters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    current_round = db.Column(db.Integer, default=1)
    current_turn_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    combatants = db.relationship("Combatant", backref="encounter")