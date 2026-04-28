from app.services import combat_engine
from app.services import encounter_service
from app.services import engine_utils

def test_next_turn(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14,
            image = "link"
        )
        combatant2 = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Monster One",
            type = "Monster",
            initiative = 12,
            max_hp = 40,
            armour_class = 11,
            image = "link"
        )

        assert encounter.current_round == 1
        assert encounter.total_turns_elapsed == 0
        combat_engine.next_turn(encounter)
        assert encounter.current_round == 1
        assert encounter.total_turns_elapsed == 1
        combat_engine.next_turn(encounter)
        assert encounter.total_turns_elapsed == 2
        assert encounter.current_round == 2

def test_get_active_combatant(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14,
            image = "link"
        )
        combatant2 = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Monster One",
            type = "Monster",
            initiative = 12,
            max_hp = 40,
            armour_class = 11,
            image = "link"
        )

        combatants = engine_utils.get_sorted_combatants(encounter.id)
        assert combat_engine.get_active_combatant(encounter, combatants) == combatant
        combat_engine.next_turn(encounter)
        assert combat_engine.get_active_combatant(encounter, combatants) == combatant2

def test_get_sorted_combatants(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14,
            image = "link"
        )
        combatant2 = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Monster One",
            type = "Monster",
            initiative = 12,
            max_hp = 40,
            armour_class = 11,
            image = "link"
        )
        combatant3 = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Monster One",
            type = "Monster",
            initiative = 20,
            max_hp = 30,
            armour_class = 11,
            image = "link"
        )

        combatants = engine_utils.get_sorted_combatants(encounter.id)
        assert combatants[0] == combatant3
        assert combatants[1] == combatant
        assert combatants[2] == combatant2