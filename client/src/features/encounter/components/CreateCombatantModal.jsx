import "./CreateCombatantModal.css";

const CreateCombatantModal = ({ onClose }) => {
  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content create-combatant-modal"
        onClick={(e) => e.stopPropagation()}
      >


        <h2 className="create-combatant-modal__title">
          Create Combatant
        </h2>


        {/* Form which takes up the bulk of the modal */}
        <form className="create-combatant-modal__form">
          {/* Name */}
          <div className="create-combatant-modal__field">
            <label>Name</label>
            <input
              type="text"
              placeholder="Enter combatant name"
            />
          </div>


          {/* Type (Player / Ally / Enemy) */}
          <div className="create-combatant-modal__field">
            <label>Type</label>

            <select defaultValue="">
              <option value="" disabled>
                Select type
              </option>

              <option value="Player">Player</option>
              <option value="Ally">Ally</option>
              <option value="Enemy">Enemy</option>
            </select>
          </div>



          {/* Max HP */}
          <div className="create-combatant-modal__field">
            <label>Max HP</label>

            <input
              type="number"
              placeholder="Enter max HP"
            />
          </div>



          {/* Armour Class */}
          <div className="create-combatant-modal__field">
            <label>Armour Class</label>

            <input
              type="number"
              placeholder="Enter armour class"
            />
          </div>



          {/* Image Upload */}
          <div className="create-combatant-modal__field">
            <label>Combatant Image</label>

            <input type="file" accept="image/*" />
          </div>



          {/* Buttons */}
          <div className="create-combatant-modal__actions">
            <button type="button">
              Create
            </button>

            <button
              type="button"
              onClick={onClose}
            >
              Close
            </button>
          </div>

        </form>
      </div>
    </div>
  );
};

export default CreateCombatantModal;