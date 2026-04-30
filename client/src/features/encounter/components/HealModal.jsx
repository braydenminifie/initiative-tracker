import "./HealModal.css";
import "./Modal.css"

const HealModal = ({ combatant, onClose }) => {
  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content heal-modal"
        onClick={(e) => e.stopPropagation()}
      >

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
        />

        {/* Buttons */}
        <div className="heal-modal__actions">
          <button className="heal-modal__button">Apply</button>
          <button className="heal-modal__button" onClick={onClose}>
            Close
          </button>
        </div>



      </div>
    </div>
  );
};

export default HealModal;