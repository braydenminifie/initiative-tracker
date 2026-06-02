import "./CreateCombatantModal.css";
import { useState } from "react";

const CreateCombatantModal = ({ onClose, encounterId, onCombatantCreated }) => {
  /* Create Combatant Form Submittion*/
  const [name, setName] = useState("");
  const [type, setType] = useState("");
  const [maxHp, setMaxHp] = useState("");
  const [armourClass, setArmourClass] = useState("");
  const [initiative, setInitiative] = useState("");
  const [imageFile, setImageFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const formData = new FormData();

      formData.append("encounter_id", encounterId);
      formData.append("name", name);
      formData.append("type", type);
      formData.append("initiative", Number(initiative));
      formData.append("max_hp", Number(maxHp));
      formData.append("armour_class", Number(armourClass));

      if (imageFile) {
        formData.append("image", imageFile);
      }

      const response = await fetch("http://localhost:5000/api/combatants", {
        method: "POST",
        body: formData, 
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Failed to create combatant");
      }

      onCombatantCreated?.(data);
      onClose();

    } catch (err) {
      console.error(err);
    }
  };


  /* Component */
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
        <form 
        className="create-combatant-modal__form"
        onSubmit={handleSubmit}
        >
          {/* Name */}
          <div className="create-combatant-modal__field">
            <label>Name</label>
            <input
              type="text"
              placeholder="Enter combatant name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>


          {/* Type (Player / Ally / Enemy) */}
          <div className="create-combatant-modal__field">
            <label>Type</label>

            <select value={type} onChange={(e) => setType(e.target.value)}>
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
              value={maxHp}
              onChange={(e) => setMaxHp(e.target.value)}
            />
          </div>



          {/* Armour Class */}
          <div className="create-combatant-modal__field">
            <label>Armour Class</label>

            <input
              type="number"
              placeholder="Enter armour class"
              value={armourClass}
              onChange={(e) => setArmourClass(e.target.value)}
            />
          </div>



          {/* Initiative */}
          <div className="create-combatant-modal__field">
            <label>Initiative</label>

            <input
              type="number"
              placeholder="Enter Initiative"
              value={initiative}
              onChange={(e) => setInitiative(e.target.value)}
            />
          </div>



          {/* Image Upload */}
          <div className="create-combatant-modal__field">
            <label>Combatant Image</label>
            <input type="file" 
            accept="image/*"
            onChange={(e) => setImageFile(e.target.files[0])}
            />
          </div>



          {/* Buttons */}
          <div className="create-combatant-modal__actions">
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

export default CreateCombatantModal;