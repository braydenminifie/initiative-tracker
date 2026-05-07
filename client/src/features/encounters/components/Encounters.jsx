import Header from "../../../components/Header"
import Hero from "../../../components/Hero"
import bird1 from "../../../assets/gecko.JPG"

import EncountersGrid from "./EncountersGrid"
import Button from "../../../components/Button"
import "./Encounters.css"

function Encounters() {
    const encounters = [{
            id: 1,
            name: "Bird Battle!",
            turnsPlayed: 2
        },
        {
            id: 2,
            name: "Armadillo Arena!",
            turnsPlayed: 3

        }]
    
    return (

    <div className = "encounters-page">
      <Header />
      <Hero
        image={bird1}
        title="Encounters"
        subtitle="Navigate your encounters here"
        />
        
        <EncountersGrid encounters = {encounters}></EncountersGrid>
        <Button variant = "new_encounter" 
            onClick = {() => {openModal("combatant", null);}}>
                +
        </Button>
    
    </div>
  )
}

export default Encounters