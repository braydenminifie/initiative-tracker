import React from "react";
import "./CombatantCard.css";
import Button from "./Button"

const CombatantCard = ({ combatant, onOpenModal }) => {
  return (
    <div className="combatant-card">
      
      {/*Left: Image*/}
      <div className="combatant-card__image">
        <img src={combatant.image} alt={combatant.name} />
      </div>

      {/*Right: Content*/}
      <div className="combatant-card__content">

        <div>
          <h3 className="combatant-card__title">{combatant.name}</h3>
          <p className="combatant-card__subtitle">{combatant.type}</p>
        </div>

        <div className="combatant-card__stats">
          <div>
            <span>HP</span>
            <strong>{combatant.hp} / {combatant.max_hp}</strong>
          </div>

          <div>
            <span>Init</span>
            <strong>{combatant.initiative}</strong>
          </div>

          <div>
            <span>AC</span>
            <strong>{combatant.ac}</strong>
          </div>
        </div>

        <div className="combatant-card__buttons">
          <Button onClick = {() => {onOpenModal("damage", combatant);
          }}> Damage </Button>

          <Button onClick = {() => {onOpenModal("heal", combatant);
          }}> Heal </Button>

          <Button> Conditions </Button>
        </div>

      </div>
    </div>
  );
};

export default CombatantCard;