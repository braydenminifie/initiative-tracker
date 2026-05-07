import Header from "../../../components/Header"
import Hero from "../../../components/Hero"
import bird1 from "../../../assets/bird1.JPG"

import EncountersGrid from "./EncountersGrid"

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

    <>
      <Header />
      <Hero
        image={bird1}
        title="Encounters"
        subtitle="Navigate your encounters here"
        />
        <EncountersGrid encounters = {encounters}></EncountersGrid>

    </>
  )
}

export default Encounters