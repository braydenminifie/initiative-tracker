from app.services import condition_service
from app.services import encounter_service
from app.services import combat_engine
from app.extensions import db

def test_create_condition(app):
    with app.app_context():
        condition = condition_service.create_condition("Test Condition", "Test Description", True)

        assert condition.name == "Test Condition"
        assert condition.description == "Test Description"
        assert condition.is_debuff == True
        assert condition.id is not None


def test_apply_condition(app):
    with app.app_context():
        condition = condition_service.create_condition("Test Condition", "Test Description", True)
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )

        #Testing application of condition
        combat_condition = condition_service.apply_condition(
            combatant_id = combatant.id,
            condition_id = condition.id,
            current_round = 2,
            current_turn_index = 3,
            duration_turns = 10 #TODO: Implement getTurnsPerRound function
        )

        assert combat_condition.duration_turns == 10
        assert combat_condition.combatant_id == combatant.id
        assert combat_condition.condition_id == condition.id
        assert combat_condition.id is not None

        #Testing re-application of the same condition, with a new duration
        reapplied_combat_condition = condition_service.apply_condition(
            combatant_id = combatant.id,
            condition_id = condition.id,
            current_round = 2,
            current_turn_index = 3,
            duration_turns = 15 
        )

        assert combat_condition.id == reapplied_combat_condition.id
        assert reapplied_combat_condition.duration_turns == 15
        assert reapplied_combat_condition.combatant_id == combatant.id
        assert reapplied_combat_condition.condition_id == condition.id

def test_update_combatant_condition_duration(app):
    with app.app_context():
        condition = condition_service.create_condition("Test Condition", "Test Description", True)
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )

        combat_condition = condition_service.apply_condition(
            combatant_id = combatant.id,
            condition_id = condition.id,
            current_round = 2,
            current_turn_index = 3,
            duration_turns = 10 
        )

        assert combat_condition.duration_turns == 10
        condition_service.update_combatant_condition_duration( 
            combatant_id = combatant.id,
            condition_id = condition.id,
            duration_turns = 12)
        assert combat_condition.duration_turns == 12

def test_decrement_condition_durations(app):
    with app.app_context():
        condition = condition_service.create_condition("Test Condition", "Test Description", True)
        condition2 = condition_service.create_condition("Test Condition 2", "Test Description", True)
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )
        combatant2 = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Monster One",
            type = "Monster",
            initiative = 12,
            max_hp = 40,
            armour_class = 11
        )

        combat_condition1 = condition_service.apply_condition(
            combatant_id = combatant.id,
            condition_id = condition.id,
            current_round = 2,
            current_turn_index = 0,
            duration_turns = 10 
        )

        combat_condition2 = condition_service.apply_condition(
            combatant_id = combatant2.id,
            condition_id = condition2.id,
            current_round = 2,
            current_turn_index = 0,
            duration_turns = 1
        )

        assert encounter.current_turn_index == 0
        combat_engine.next_turn(encounter)
        assert encounter.current_turn_index == 1

        assert combat_condition1.is_active == True
        assert combat_condition2.is_active == False