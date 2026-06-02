from ..models.combatant_condition import CombatantCondition
from ..models.condition import Condition
from ..extensions import db
from .engine_utils import get_sorted_combatants
from .encounter_service import get_encounter

#Services for handling conditions

def get_all_conditions():
    return Condition.query.all()



def get_condition_by_id(id):
    condition = Condition.query.filter_by(id=id).first()
    return condition



def get_combatant_conditions_by_combatant_id(id):
    conditions = CombatantCondition.query.filter_by(combatant_id=id).all()
    return conditions



def get_combatant_condition(combatant_id, condition_id):
    cc = CombatantCondition.query.filter_by(
        combatant_id=combatant_id,
        condition_id=condition_id,
        is_active=True).first()
    return cc



def create_condition(name, description, is_debuff):
    condition = Condition(
        name = name, 
        description = description, 
        is_debuff = is_debuff)
    db.session.add(condition)
    db.session.commit()
    return condition



def delete_condition(id):
    condition = get_condition_by_id(id)
    if not condition:
        raise ValueError("Condition not found")
    
    else:
        db.session.delete(condition)
        db.session.commit()
        return True



def apply_condition(
    combatant_id,
    condition_id,
    encounter_id,
    current_round,
    current_turn,
    duration_turns=None,
    
):
    #If the condition already exists on the combatant, refresh the condition timing
    existing = get_combatant_condition(combatant_id, condition_id)
    encounter = get_encounter(encounter_id)
    print(encounter)

    if existing:
        existing.duration_turns = duration_turns
        existing.applied_round = current_round
        existing.applied_turn = current_turn
        existing.applied_total_turn - encounter.total_turns_elapsed

        db.session.commit()
        return existing

    #Otherwise, apply the new condition
    else:
        cc = CombatantCondition(
            combatant_id=combatant_id,
            condition_id=condition_id,
            duration_turns=duration_turns,
            applied_round=current_round,
            applied_turn=current_turn,
            applied_total_turn= encounter.total_turns_elapsed,
            is_active=True
        )

        db.session.add(cc)
        db.session.commit()
        return cc
    
    

def remove_condition_from_combatant(combatant_id, condition_id):
    condition = CombatantCondition.query.filter_by(
        combatant_id = combatant_id, 
        condition_id = condition_id)
    
    if not condition:
        raise ValueError("Combatant's Condition not found")
    
    else:
        db.session.delete(condition)
        db.session.commit()
        return True



def update_combatant_condition_duration(combatant_id, condition_id, duration_turns):
    cc = get_combatant_condition(combatant_id, condition_id)

    if not cc:
        raise ValueError("Condition not found")
    
    cc.duration_turns = duration_turns
    db.session.commit()
    return cc



#Called at the end of each turn in combat_engine.py
#Expires combatant conditions based on turn progression
def decrement_condition_durations(encounter):
    conditions = CombatantCondition.query.filter_by(is_active=True).all()

    for cc in conditions:
        turns_passed = encounter.total_turns_elapsed - cc.applied_total_turn

        if turns_passed >= cc.duration_turns:
            cc.is_active = False

    db.session.commit()

