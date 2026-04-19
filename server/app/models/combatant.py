from ..extensions import db

class Combatant(db.Model):
    __tablename__ = "combatants"

    id = db.Column(db.Integer, primary_key=True)
    encounter_id = db.Column(
        db.Integer,
        db.ForeignKey("encounters.id")
    )
    name = db.Column(db.String(100))
    type = db.Column(db.String())
    initiative = db.Column(db.Integer)
    max_hp = db.Column(db.Integer)
    current_hp = db.Column(db.Integer)
    armour_class = db.Column(db.Integer)
    is_alive = db.Column(db.Boolean, default=True)