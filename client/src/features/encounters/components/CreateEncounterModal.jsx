import { useState } from "react";
import "./CreateEncounterModal.css";


const CreateEncounterModal = ({ onClose, onEncounterCreated }) => {
  const [name, setName] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/api/encounters", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Failed to create encounter");
      }

      onEncounterCreated(data);
      onClose();


    } catch (err) {
      console.error(err);
    }
  };

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
        <form 
        className="create-encounter-modal__form"
        onSubmit = {handleSubmit}
        >
          
          {/* Encounter Name */}
          <div className="create-encounter-modal__field">
            <label>Encounter Name</label>

            <input
              type="text"
              placeholder="Enter encounter name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          {/* Buttons */}
          <div className="create-encounter-modal__actions">
            <button type="submit">
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