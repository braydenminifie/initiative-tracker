import "./DamageModal.css";
import "./Modal.css";
import { useState } from "react";
import piwakawaka from "../assets/piwakawaka.jpg"

const DamageModal = ({ combatant, onClose, onDamage }) => {
  /* Handle Damage */
  const [damage, setDamage] = useState("");

  const handleDamage = async () => {
    const damageAmount = parseInt(damage);
    const newHealth = Math.max(0, combatant.hp - damageAmount);

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
      onDamage(updatedCombatant);
      onClose();


    } catch (error) {
      console.error("Failed to apply damage:", error);
    }
  };



  /* Component */
  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content damage-modal"
        onClick={(e) => e.stopPropagation()}
      >
        <h1>Damage!</h1>

        <img
          src={piwakawaka}
          alt={combatant.name}
          className="damage-modal__image"
        />

        <h2 className="damage-modal__name">{combatant.name}</h2>
        <p className="damage-modal__hp">HP: {combatant.hp} / {combatant.max_hp}</p>

        <input
          type="number"
          placeholder="Damage amount"
          className="damage-modal__input"
          value = {damage}
          onChange={(e) => setDamage(e.target.value)}
        />

        {/* Buttons */}
        <div className="damage-modal__actions">
          <button 
          className="damage-modal__button"
          onClick = {handleDamage}
          >
            Apply
          </button>
          <button className="damage-modal__button" onClick={onClose}>
            Close
          </button>
        </div>



      </div>
    </div>
  );
}

export default DamageModal;