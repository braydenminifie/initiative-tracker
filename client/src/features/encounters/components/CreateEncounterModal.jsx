import "./CreateEncounterModal.css";

const CreateEncounterModal = ({ onClose }) => {
  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content create-encounter-modal"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="create-encounter-modal__title">
          Create Encounter
        </h2>


        {/* Form which takes up the bulk of the modal */}
        <form className="create-encounter-modal__form">
          
          {/* Encounter Name */}
          <div className="create-encounter-modal__field">
            <label>Encounter Name</label>

            <input
              type="text"
              placeholder="Enter encounter name"
            />
          </div>

          {/* Buttons */}
          <div className="create-encounter-modal__actions">
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

export default CreateEncounterModal;