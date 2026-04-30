import React, {useState} from "react";
import CombatantCard from "./CombatantCard";
import HealModal from "./HealModal"
import "./CombatantGrid.css";



const CombatantGrid = ({ combatants = [] }) => {
  {/* State for handling modals*/}
  const [activeModal, setActiveModal] = useState();

  const openModal = (type, combatant) => {
    setActiveModal({type, combatant})
  };
  
  const closeModal = () => {
    setActiveModal(null);
  }


  return (
    <>
      <section className="combatant-grid">
        {combatants.map((c) => (
          <CombatantCard key={c.id} 
          combatant={c} 
          onOpenModal = {openModal}/>
        ))}
      </section>


      {/* Checks for rendering modal */}
      {activeModal?.type === "heal" && (
        <HealModal
          combatant={activeModal.combatant}
          onClose={closeModal}
        />
      )}

    </>
  );
};

export default CombatantGrid;