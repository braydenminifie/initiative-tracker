import "./HealModal.css";
import "./Modal.css"
import { useState } from "react";

const HealModal = ({ combatant, onClose, onHeal }) => {
  /* Handle Heal */
  const [heal, setHeal] = useState("");
  
    const handleHeal = async () => {
      const healAmount = parseInt(heal);
      const newHealth = Math.max(0, combatant.hp + healAmount);
  
       try {
        const response = await fetch(
          `http://127.0.0.1:5000/api/combatants/${combatant.id}/health`,
          {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              health: newHealth,
            }),
          }
        );
  
        const updatedCombatant = await response.json();
        onHeal(updatedCombatant);
        onClose();
  
  
      } catch (error) {
        console.error("Failed to apply heal:", error);
      }
    };

  /* Heal Component */
  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content heal-modal"
        onClick={(e) => e.stopPropagation()}
      >

        <h1>Heal!</h1>
        <img
          src={combatant.image}
          alt={combatant.name}
          className="heal-modal__image"
        />

        <h2 className="heal-modal__name">{combatant.name}</h2>
        <p className="heal-modal__hp">HP: {combatant.hp} / {combatant.max_hp}</p>

        <input
          type="number"
          placeholder="Heal amount"
          className="heal-modal__input"
          value = {heal}
          onChange={(e) => setHeal(e.target.value)}
        />

        {/* Buttons */}
        <div className="heal-modal__actions">
          <button 
          className="heal-modal__button"
          onClick = {handleHeal}
          >
            Apply
            </button>
          <button className="heal-modal__button" onClick={onClose}>
            Close
          </button>
        </div>



      </div>
    </div>
  );
};

export default HealModal;