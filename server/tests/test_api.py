def test_create_encounter_success(client):
    response = client.post("/api/encounters", json={
        "name": "Goblin Fight"
    })

    assert response.status_code == 201

    data = response.get_json()
    assert data["name"] == "Goblin Fight"
    assert data["round"] == 1
    assert "id" in data



def test_create_combatant_success(client):
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
        "armour_class": 14
    })
    assert response.status_code == 201

    data = response.get_json()
    assert data["name"] == "Goblin"
    assert "id" in data




def test_next_turn_success(client, app):
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
        "armour_class": 14
    })
    assert response.status_code == 201

    response = client.post(f"/api/encounters/{encounter_id}/next-turn")
    assert response.status_code == 200

    data = response.get_json()
    print(data)
    assert data is not None
    assert "round" in data or "current_turn_index" in data
