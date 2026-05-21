import { useState, useEffect } from "react";

import Header from "../../../components/Header"
import Hero from "../../../components/Hero"
import bird1 from "../../../assets/gecko.JPG"

import EncountersGrid from "./EncountersGrid"
import CreateEncounterModal from "./CreateEncounterModal";
import Button from "../../../components/Button"
import "./Encounters.css"

function Encounters() {
    const [encounters, setEncounters] = useState([]);
    const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);

    //This function is passed to the CreateEncounterModal component
    const handleEncounterCreated = (newEncounter) => {
      setEncounters((prev => [...prev, newEncounter]));
    };

    useEffect(() => {
        fetch("http://localhost:5000/api/encounters")
        .then((res) => res.json())
        .then((data) => {
        setEncounters(data);
      })
      .catch((err) => {
        console.error("Failed to fetch encounters:", err);
      });
    }, []);



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
            onClick={() => setIsCreateModalOpen(true)}>
                +
        </Button>


        {isCreateModalOpen && (
            <CreateEncounterModal
                onClose={() => setIsCreateModalOpen(false)}
                onEncounterCreated = {handleEncounterCreated}
            />
        )}
    
    </div>
  )
}

export default Encounters