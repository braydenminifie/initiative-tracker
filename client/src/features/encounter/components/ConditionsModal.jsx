import "./ConditionsModal.css";
import piwakawaka from "../assets/piwakawaka.jpg"

import { useState, useEffect } from "react"

const ConditionsModal = ({ combatant, encounterId, currentRound, currentTurn, onClose, onConditionApplied }) => {
  const [allConditions, setAllConditions] = useState([]);
  const [selectedConditionId, setSelectedConditionId] = useState("");
  const [duration, setDuration] = useState(1);
  const API_BASE = "http://localhost:5000";

  {/* Fetch all conditions for the conditions list */}
  useEffect(() => {
    fetch("http://localhost:5000/api/conditions")
      .then((res) => res.json())
      .then((data) => setAllConditions(data))
      .catch((err) =>
        console.error("Failed to fetch conditions:", err)
      );
  }, []);



  {/* Apply the chosen condition */}
  const handleApplyCondition = async () => {
    if (!selectedConditionId) return;

    try {
      const response = await fetch(
        `http://localhost:5000/api/combatants/${combatant.id}/apply-condition`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            condition_id: Number(selectedConditionId),
            encounter_id: Number(encounterId),
            duration: Number(duration),
            current_round: currentRound,
            current_turn: currentTurn,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Failed to apply condition");
      }

      onConditionApplied(combatant.id, data);
      onClose();

    } catch (err) {
      console.error(err);
    }
  };



  return (
    <div className="modal" onClick={onClose}>
      <div
        className="modal__content conditions-modal"
        onClick={(e) => e.stopPropagation()}
      >

        {/* Header */}
        <div className="conditions-modal__header">
          <img src={`${API_BASE}${combatant.image}`}
            alt={combatant.name}
            className="conditions-modal__image"
          />

          <h2 className="conditions-modal__name">
            {combatant.name}
          </h2>
        </div>

        {/* Apply Condition Section*/}
        <div className="conditions-modal__apply">
          <select
            value={selectedConditionId}
            onChange={(e) =>
              setSelectedConditionId(e.target.value)
            }
          >
            <option value="">Select Condition</option>
            {allConditions.map((condition) => (
              <option key={condition.id} value={condition.id}>
                {condition.name}
              </option>
            ))}
          </select>

          <input
            type="number"
            min="1"
            value={duration}
            onChange={(e) => setDuration(e.target.value)}
          />

          <button onClick={handleApplyCondition}>
            Apply
          </button>
        </div>

        {/* Conditions List */}
        {/* If combatant has no conditions, shows "No active conditions" instead of a list */}
        <div className="conditions-modal__list">
          {combatant.conditions && combatant.conditions.length > 0 ? (
            combatant.conditions.map((condition) => (
              <div
                key={condition.id}
                className="conditions-modal__item"
              >
                <div className="conditions-modal__item-header">
                  <span className="conditions-modal__item-name">
                    {condition.name}
                  </span>
                  <span className="conditions-modal__item-duration">
                    {condition.duration} turns
                  </span>
                </div>

                <p className="conditions-modal__item-description">
                  {condition.description}
                </p>
              </div>
            ))
          ) : (
            <p className="conditions-modal__empty">
              No active conditions
            </p>
          )}
        </div>



        {/* Close Button */}
        <button
          className="conditions-modal__close"
          onClick={onClose}
        >
          Close
        </button>
      </div>
    </div>
  );
};

export default ConditionsModal;