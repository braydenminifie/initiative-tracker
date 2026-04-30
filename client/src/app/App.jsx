import { useState, useEffect } from 'react'
import axios from "axios"
import bird1 from "../assets/bird1.JPG"
import kereru from "../features/encounter/assets/kereru.JPG"
import piwakawaka from "../features/encounter/assets/piwakawaka.JPG"

import Header from "../components/Header"
import Hero from "../components/Hero"
import CombatantGrid from "../features/encounter/components/CombatantGrid"

function App() {
  const combatants = [
  {
    id: 1,
    name: "piwakawaka",
    type: "Monster",
    hp: 7,
    max_hp: 7,
    initiative: 12,
    ac: 13,
    image: piwakawaka
  },
  {
    id: 2,
    name: "kereru",
    type: "Monster",
    hp: 20,
    max_hp: 20,
    initiative: 18,
    ac: 12,
    image: kereru
  },
  {
    id: 3,
    name: "kereru",
    type: "Monster",
    hp: 20,
    max_hp: 20,
    initiative: 18,
    ac: 12,
    image: kereru
  },
  {
    id: 4,
    name: "kereru",
    type: "Monster",
    hp: 20,
    max_hp: 20,
    initiative: 18,
    ac: 12,
    image: kereru
  },
  {
    id: 5,
    name: "kereru",
    type: "Monster",
    hp: 20,
    max_hp: 20,
    initiative: 18,
    ac: 12,
    image: kereru
  },
];


  return (
    <>
      <Header />
      <Hero
        image={bird1}
        title="Bird Fight"
        subtitle="Ambushed by a group of birds!"
        />
      <CombatantGrid combatants={combatants}/>


    </>
  )
}

export default App
