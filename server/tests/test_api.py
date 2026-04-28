def test_create_encounter_success(client):
    response = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    })

    assert response.status_code == 201

    data = response.get_json()
    assert data["name"] == "Goblin Fight"
    assert data["round"] == 1
    assert "id" in data



def test_create_combatant(client):
    #Create an encounter (foreign key dependency)
    encounter_response = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    })
    assert encounter_response.status_code == 201
    encounter_id = encounter_response.get_json()["id"]


    #Create combatant
    response = client.post("/api/combatants", json={
        "encounter_id": encounter_id,
        "name": "Goblin",
        "type": "enemy",
        "initiative": 15,
        "max_hp": 20,
        "armour_class": 14,
        "image": "link"
    })
    assert response.status_code == 201

    data = response.get_json()
    assert data["name"] == "Goblin"
    assert "id" in data



def test_get_combatant(client):
    #Create an encounter (foreign key dependency)
    encounter_response = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    })
    encounter_id = encounter_response.get_json()["id"]


    #Create combatant
    combatant = client.post("/api/combatants", json={
        "encounter_id": encounter_id,
        "name": "Goblin",
        "type": "enemy",
        "initiative": 15,
        "max_hp": 20,
        "armour_class": 14,
        "image": "link"
    })
    data = combatant.get_json()
    combatant_id = data["id"]

    #Fetch combatant
    response = response = client.get(f"/api/combatants/{combatant_id}")
    assert response.status_code == 200

    data = response.get_json()
    assert data["name"] == "Goblin"
    assert data["id"] == combatant_id



def test_next_turn(client):
    #Create an encounter
    response = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    })
    assert response.status_code == 201
    encounter = response.get_json()
    encounter_id = encounter["id"]

    #Create a combatant in the encounter
    response = client.post("/api/combatants", json={
        "encounter_id": encounter_id,
        "name": "Gandalf",
        "type": "Player",
        "initiative": 15,
        "max_hp": 200,
        "armour_class": 14,
        "image": "link"
    })
    assert response.status_code == 201

    response = client.post(f"/api/encounters/{encounter_id}/next-turn")
    assert response.status_code == 200

    data = response.get_json()
    print(data)
    assert data is not None
    assert "round" in data or "current_turn_index" in data



def test_delete_combatant(client):
    #Create an encounter (foreign key dependency)
    encounter_response = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    })
    encounter_id = encounter_response.get_json()["id"]


    #Create combatant
    combatant = client.post("/api/combatants", json={
        "encounter_id": encounter_id,
        "name": "Goblin",
        "type": "Enemy",
        "initiative": 15,
        "max_hp": 20,
        "armour_class": 14,
        "image": "link"
    })
    data = combatant.get_json()
    combatant_id = data["id"]

    #Delete combatant
    response = client.delete(f"/api/combatants/{combatant_id}")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Combatant deleted"



def test_update_combatant_health(client):
    #Create encounter
    encounter = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    }).get_json()

    #Create combatant
    combatant = client.post("/api/combatants", json={
        "encounter_id": encounter["id"],
        "name": "Goblin",
        "type": "Enemy",
        "initiative": 10,
        "max_hp": 20,
        "armour_class": 12,
        "image": "link"
    }).get_json()

    combatant_id = combatant["id"]

    #Update health
    response = client.patch(f"/api/combatants/{combatant_id}/health", json={
        "health": 15
    })

    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == combatant_id
    assert data["name"] == "Goblin"
    assert data["hp"] == 15



def test_create_condition(client):
    response = client.post("/api/conditions", json={
        "name": "Poisoned",
        "description": "Loses health each turn",
        "is_debuff": True
    })

    assert response.status_code == 201

    data = response.get_json()

    assert "id" in data
    assert data["name"] == "Poisoned"
    assert data["description"] == "Loses health each turn"
    assert data["is_debuff"] is True



def test_apply_condition(client):
    #Create encounter
    encounter = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    }).get_json()

    #Create combatant
    combatant = client.post("/api/combatants", json={
        "encounter_id": encounter["id"],
        "name": "Goblin",
        "type": "Enemy",
        "initiative": 10,
        "max_hp": 12,
        "armour_class": 13,
        "image": "link"
    }).get_json()

    combatant_id = combatant["id"]

    #Create condition
    condition = client.post("/api/conditions", json={
        "name": "Poisoned",
        "description": "Loses health each turn",
        "is_debuff": True
    }).get_json()

    #Apply condition
    response = client.post(f"/api/combatants/{combatant_id}/apply-condition", json={
        "condition_id": 1,
        "current_round": 1,
        "current_turn": 0,
        "duration": 3
    })

    assert response.status_code == 201

    data = response.get_json()

    assert "id" in data
    assert data["combatant_id"] == combatant_id
    assert data["condition_id"] == 1



def test_get_combatant_conditions(client):
    #Create encounter
    encounter = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    }).get_json()

    #Create combatant
    combatant = client.post("/api/combatants", json={
        "encounter_id": encounter["id"],
        "name": "Goblin",
        "type": "Enemy",
        "initiative": 10,
        "max_hp": 12,
        "armour_class": 13,
        "image": "link"
    }).get_json()

    combatant_id = combatant["id"]

    #Create condition
    condition = client.post("/api/conditions", json={
        "name": "Poisoned",
        "description": "Loses health each turn",
        "is_debuff": True
    }).get_json()

    #Apply condition
    cc = client.post(f"/api/combatants/{combatant_id}/apply-condition", json={
        "condition_id": 1,
        "current_round": 1,
        "current_turn": 0,
        "duration": 3
    })

    response = client.get(f"/api/combatants/{combatant_id}/conditions")
    data = response.get_json()
    conditions = data["conditions"][0]
    assert response.status_code == 200
    assert conditions["name"] == "Poisoned"



def test_get_encounter_state(client):
    #Create encounter
    encounter = client.post("/api/encounters", json={
        "name": "Test Encounter"
    }).get_json()

    encounter_id = encounter["id"]

    #Create combatants
    c1 = client.post("/api/combatants", json={
        "encounter_id": encounter_id,
         "name": "Hero",
        "type": "Player",
        "initiative": 15,
        "max_hp": 20,
        "armour_class": 15,
        "image": "link"
    }).get_json()

    c2 = client.post("/api/combatants", json={
        "encounter_id": encounter_id,
        "name": "Goblin",
        "type": "Enemy",
        "initiative": 10,
        "max_hp": 12,
        "armour_class": 13,
        "image": "link"
    }).get_json()

    #Call endpoint
    response = client.get(f"/api/encounters/{encounter_id}/state")
    data = response.get_json()

    #Assertions
    assert response.status_code == 200

    assert data["encounter"]["id"] == encounter_id
    assert data["encounter"]["name"] == "Test Encounter"
    assert data["encounter"]["round"] == 1

    assert len(data["combatants"]) == 2
    names = [c["name"] for c in data["combatants"]]
    assert "Hero" in names
    assert "Goblin" in names

    assert data["active_combatant_id"] is not None
    active = next(
        c for c in data["combatants"]
        if c["id"] == data["active_combatant_id"]
    )

    assert active["is_active"] is True