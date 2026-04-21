from app.services import encounter_service

def test_create_encounter(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        assert encounter.name == "Test Encounter"
        assert encounter.id is not None
        assert encounter.current_round == 1
        assert encounter.current_turn_index == 0
        assert encounter.is_active == True
        assert encounter.total_turns_elapsed == 0



def test_create_combatant(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )

        assert combatant.name == "Combatant One"
        assert combatant.id is not None



def test_remove_combatant(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )

        assert combatant.id is not None

        encounter_service.remove_combatant(combatant.id)

        deleted = encounter_service.get_combatant(combatant.id)
        assert deleted is None



def test_remove_encounter(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        assert encounter.id is not None

        encounter_service.remove_encounter(encounter.id)

        deleted = encounter_service.get_encounter(encounter.id)
        assert deleted is None



def test_get_encounter(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        assert encounter.id is not None

        result = encounter_service.get_encounter(encounter.id)

        assert result.id == encounter.id
        assert result.name == "Test Encounter"



def test_get_combatant(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )

        assert combatant.id is not None

        result = encounter_service.get_combatant(combatant.id)

        assert result.encounter_id == encounter.id
        assert result.id == combatant.id



def test_set_combatant_health(app):
    with app.app_context():
        encounter = encounter_service.create_encounter("Test Encounter")
        combatant = encounter_service.create_combatant(
            encounter_id = encounter.id,
            name = "Combatant One",
            type = "Player",
            initiative = 15,
            max_hp = 28,
            armour_class = 14
        )

        assert combatant.current_hp == 28
        encounter_service.set_combatant_health(combatant.id, 15)
        assert combatant.current_hp == 15
        encounter_service.set_combatant_health(combatant.id, -5)
        assert combatant.current_hp == 0
        assert combatant.is_alive == False
        encounter_service.set_combatant_health(combatant.id, 200)
        assert combatant.current_hp == 28
        assert combatant.is_alive == True
        