import "./DamageModal.css";
import "./Modal.css"

const DamageModal = ({ combatant, onClose }) => {
  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content damage-modal"
        onClick={(e) => e.stopPropagation()}
      >
        <h1>Damage!</h1>

        <img
          src={combatant.image}
          alt={combatant.name}
          className="damage-modal__image"
        />

        <h2 className="damage-modal__name">{combatant.name}</h2>
        <p className="damage-modal__hp">HP: {combatant.hp} / {combatant.max_hp}</p>

        <input
          type="number"
          placeholder="Damage amount"
          className="damage-modal__input"
        />

        {/* Buttons */}
        <div className="damage-modal__actions">
          <button className="damage-modal__button">Apply</button>
          <button className="damage-modal__button" onClick={onClose}>
            Close
          </button>
        </div>



      </div>
    </div>
  );
};

export default DamageModal;