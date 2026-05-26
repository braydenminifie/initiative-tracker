import { useState, useEffect } from 'react'
import { useParams } from "react-router-dom"
import axios from "axios"

import bird1 from "../../../assets/bird1.JPG"

import Header from "../../../components/Header"
import Hero from "../../../components/Hero"
import CombatantGrid from "../components/CombatantGrid"

function Encounter() {
  const [encounter, setEncounter] = useState(null);
  const [combatants, setCombatants] = useState([]);
  const [activeCombatantId, setActiveCombatantId] = useState(null);
  const [round, setRound] = useState(null);
  const [turn, setTurn] = useState(null);

  const { id } = useParams();
  
   useEffect(() => {
    fetch(`http://localhost:5000/api/encounters/${id}/state`)
      .then((res) => res.json())
      .then((data) => {
        setEncounter(data.encounter);
        setCombatants(data.combatants);
        setActiveCombatantId(data.active_combatant_id);
        setRound(data.encounter.round);
        setTurn(data.encounter.turn_index)
      })
      .catch((err) => {
        console.error("Failed to fetch encounter:", err);
      });
  }, [id]);

  return (
    <>
      <Header />
      <Hero
        image={bird1}
        title={encounter?.name || "Loading..."}
        subtitle=""
        />
      <CombatantGrid combatants={combatants}
      setCombatants={setCombatants}
      encounterId={id}
      currentRound={round}
      currentTurn={turn}
      
      />


    </>
  )
}

export default Encounter
