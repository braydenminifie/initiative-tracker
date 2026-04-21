from ..models.combatant import Combatant
from ..extensions import db
from .condition_service import decrement_condition_durations
from .engine_utils import get_sorted_combatants

#Services for handling the core gameplay loop



def get_active_combatant(encounter, combatants):
    if not combatants:
        return None

    index = encounter.current_turn_index
    return combatants[index]



#Advances turn
def next_turn(encounter):

    #Skip if all combatants are dead
    combatants = get_sorted_combatants(encounter.id)
    alive = [c for c in combatants if c.is_alive]
    if not alive:
        return {"status": "encounter_over"}

    #Move to the next turn 
    encounter.total_turns_elapsed += 1
    if encounter.current_turn_index >= len(alive):
        next_round(encounter)

    else:
        encounter.current_turn_index += 1
        db.session.commit()

    #Decrement all conditions by 1 turn
    decrement_condition_durations(encounter)
    return encounter



def next_round(encounter):
    encounter.current_round += 1
    encounter.current_turn_index = 0
    db.session.commit()
