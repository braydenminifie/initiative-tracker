from ..extensions import db

class Condition(db.Model):
    __tablename__ = "conditions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    is_debuff = db.Column(db.Boolean)