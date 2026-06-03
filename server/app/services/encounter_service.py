from ..extensions import db
from ..models.combatant import Combatant
from ..models.encounter import Encounter
from ..models.combatant_condition import CombatantCondition
from ..services.engine_utils import get_sorted_combatants

#Services for setting up and handling each encounter

def create_encounter(name: str):
    encounter = Encounter(
        name = name,
        current_round = 1,
        current_turn_index = 0,
        is_active = True,
        total_turns_elapsed = 0)

    db.session.add(encounter)
    db.session.commit()

    return encounter



def create_combatant(
        encounter_id: int,
        name: str,
        type: str,
        initiative: int,
        max_hp: int,
        armour_class: int,
        image: str
        ):
    combatant = Combatant(
        encounter_id = encounter_id,
        name = name,
        type = type,
        initiative = initiative,
        max_hp = max_hp,
        current_hp = max_hp,
        armour_class = armour_class,
        is_alive = True,
        image = image
    )
    
    db.session.add(combatant)
    db.session.commit()

    return combatant
    


def remove_combatant(id: int):
    combatant = get_combatant(id)

    if not combatant:
        raise ValueError("Combatant not found")
    
    db.session.delete(combatant)
    db.session.commit()

    return combatant



def remove_encounter(id: int):
    encounter = get_encounter(id)

    if not encounter:
        raise ValueError("Encounter not found")
    
    db.session.delete(encounter)
    db.session.commit()



def get_encounter(id: int):
    encounter = db.session.query(Encounter).filter(Encounter.id == id).first()
    return encounter



def get_all_encounters():
    encounters = db.session.query(Encounter).all()
    return encounters



def get_combatant(id: int):
    combatant = db.session.query(Combatant).filter(Combatant.id == id).first()
    return combatant



def set_combatant_health(id: int, health: int):
    combatant = db.session.query(Combatant).filter(Combatant.id == id).first()

    if not combatant:
        return combatant

    if health > combatant.max_hp:
        combatant.current_hp = combatant.max_hp
    elif health < 0:
        combatant.current_hp = 0
    else:
        combatant.current_hp = health
    
    combatant.is_alive = combatant.current_hp > 0
    db.session.commit()
    return combatant



#This large function returns the entire encounter state for the get_encounter_state_route
def get_encounter_state(encounter_id):
    encounter = db.session.get(Encounter, encounter_id)
    if not encounter:
        return None

    combatants = get_sorted_combatants(encounter_id)
    alive = [c for c in combatants if c.is_alive]
    active = None
    if alive:
        index = encounter.current_turn_index % len(alive)
        active = alive[index]

    combatant_list = []
    for c in combatants:
        combatant_conditions = CombatantCondition.query.filter_by(
            combatant_id=c.id,
            is_active=True
        ).all()

        combatant_list.append({
            "id": c.id,
            "name": c.name,
            "hp": c.current_hp,
            "type": c.type,
            "max_hp": c.max_hp,
            "is_alive": c.is_alive,
            "initiative": c.initiative,
            "armour_class": c.armour_class,
            "image": c.image,
            "is_active": active and c.id == active.id,

            "conditions": [
                {
                    "id": cc.id,
                    "name": cc.condition.name,
                    "duration": cc.duration_turns,
                    "description": cc.condition.description,
                    "applied_total_turn": cc.applied_total_turn
                }
                for cc in combatant_conditions
            ]
        })

    return {
        "encounter": {
            "id": encounter.id,
            "name": encounter.name,
            "round": encounter.current_round,
            "turn_index": encounter.current_turn_index,
            "is_active": encounter.is_active,
            "total_turns_elapsed": encounter.total_turns_elapsed
        },
        "active_combatant_id": active.id if active else None,
        "combatants": combatant_list
    }