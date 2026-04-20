from ..extensions import db
from ..models.combatant import Combatant
from ..models.encounter import Encounter

#Services for setting up and handling each encounter

def create_encounter(name: str):
    encounter = Encounter(
        name = name,
        current_round = 1,
        current_turn_index = 0,
        is_active = True)

    db.session.add(encounter)
    db.session.commit()

    return encounter



def create_combatant(
        encounter_id: int,
        name: str,
        type: str,
        initiative: int,
        max_hp: int,
        armour_class: int
        ):
    combatant = Combatant(
        encounter_id = encounter_id,
        name = name,
        type = type,
        initiative = initiative,
        max_hp = max_hp,
        current_hp = max_hp,
        armour_class = armour_class,
        is_alive = True
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



def remove_encounter(id: int):
    encounter = get_encounter(id)

    if not encounter:
        raise ValueError("Encounter not found")
    
    db.session.delete(encounter)
    db.session.commit()



def get_encounter(id: int):
    encounter = db.session.query(Encounter).filter(Encounter.id == id).first()
    return encounter



def get_combatant(id: int):
    combatant = db.session.query(Combatant).filter(Combatant.id == id).first()
    return combatant