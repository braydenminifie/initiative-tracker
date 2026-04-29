import React from "react";
import CombatantCard from "./CombatantCard";
import "./CombatantGrid.css";


const CombatantGrid = ({ combatants = [] }) => {
  return (
    <section className="combatant-grid">
      {combatants.map((c) => (
        <CombatantCard key={c.id} combatant={c} />
      ))}
    </section>
    
  );
};

export default CombatantGrid;