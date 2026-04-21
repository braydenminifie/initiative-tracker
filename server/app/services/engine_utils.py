from ..models.combatant import Combatant

def get_sorted_combatants(encounter_id):
    return (Combatant.query.filter_by(encounter_id=encounter_id)
        .order_by(Combatant.initiative.desc())
        .all()
    )
