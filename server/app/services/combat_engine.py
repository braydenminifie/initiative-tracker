from ..models.combatant import Combatant

#Services for handling the core gameplay loop

def get_sorted_combatants(encounter_id):
    return (Combatant.query.filter_by(encounter_id=encounter_id)
        .order_by(Combatant.initiative.desc())
        .all()
    )

def get_active_combatant(encounter, combatants):
    if not combatants:
        return None

    index = encounter.current_turn_index
    return combatants[index]

from ..extensions import db

#Advances turn
def next_turn(encounter):
    combatants = get_sorted_combatants(encounter.id)

    #Skip dead combatants
    alive = [c for c in combatants if c.is_alive]
    if not alive:
        return {"status": "encounter_over"}


    #Check if end of round
    if encounter.current_turn_index >= len(alive):
        next_round(encounter)
        #TODO: Call tick conditions function once implemented

    else:
        encounter.current_turn_index += 1
        db.session.commit()

    
    return {
        "current_round": encounter.current_round,
        "current_turn_index": encounter.current_turn_index,
        "active_combatant": alive[encounter.current_turn_index].name
    }

def next_round(encounter):
    encounter.current_round += 1
    encounter.current_turn_index = 0
    db.session.commit()
