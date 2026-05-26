import React, {useState} from "react";
import CombatantCard from "./CombatantCard";
import HealModal from "./HealModal";
import DamageModal from "./DamageModal";
import ConditionsModal from "./ConditionsModal";
import CreateCombatantModal from "./CreateCombatantModal";
import Button from "../../../components/Button";


import "./CombatantGrid.css";



const CombatantGrid = ({ combatants = [], setCombatants, encounterId, currentRound, currentTurn }) => {
  {/* State for handling modals*/}
  const [activeModal, setActiveModal] = useState();

  const openModal = (type, combatant) => {
    setActiveModal({type, combatant})
  };
  
  const closeModal = () => {
    setActiveModal(null);
  }


  /* Update Health for a Combatant */
  const updateHealth = (updatedCombatant) => {
  const updatedCombatants = combatants.map((combatant) => {
    const isTarget = combatant.id === updatedCombatant.id;

    if (isTarget) {
      return {
        ...combatant,
        hp: updatedCombatant.hp,
      };
    }

    return combatant;
  });

  setCombatants(updatedCombatants);
};

  /* Update combatants list when a new combatant is created */
  const handleCombatantCreated = (newCombatant) => {
    setCombatants((prev) =>
      [...prev, newCombatant].sort(
        (a, b) => b.initiative - a.initiative
      )
    );
  };

  /* Returned Component */
  return (
    <>
      <section className="combatant-grid">
        {combatants.map((c) => (
          <CombatantCard key={c.id} 
          combatant={c} 
          onOpenModal = {openModal}/>
        ))}
      </section>

      <Button variant = "new_combatant" 
      onClick = {() => {openModal("combatant", null);}}>
        +
        </Button>

      {/* Checks for rendering modal */}
      {activeModal?.type === "heal" && (
        <HealModal
          combatant={activeModal.combatant}
          onClose={closeModal}
          onHeal={updateHealth}
        />
      )}

      {activeModal?.type === "damage" && (
        <DamageModal
          combatant={activeModal.combatant}
          onClose={closeModal}
          onDamage={updateHealth}
        />
      )}

      {activeModal?.type === "conditions" && (
        <ConditionsModal
          combatant={activeModal.combatant}
          currentRound={currentRound}
          currentTurn={currentTurn}
          onClose={closeModal}
        />
      )}

      {activeModal?.type === "combatant" && (
        <CreateCombatantModal
          onClose={closeModal}
          encounterId={encounterId}
          onCombatantCreated={handleCombatantCreated}
        />
      )}

    </>
  );
};

export default CombatantGrid;