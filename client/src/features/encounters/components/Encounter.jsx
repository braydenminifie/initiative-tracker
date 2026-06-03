import "./Encounter.css";
import { Link } from "react-router-dom";
import Button from "../../../components/Button"

const Encounter = ({ encounter, onDelete }) => {
  /* Component */
  return (
    <div className="encounter-card">
      <Link to={`/encounters/${encounter.id}`} className="encounter-link">
        <div className="encounter-card__content">
          <h2>{encounter.name}</h2>
          <p>Turns Played: {encounter.turn}</p>
        </div>
      </Link>

      <Button
        variant="delete_encounter"
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          onDelete(encounter.id)
        }}
      >
      -
      </Button>
    </div>
  );
};

export default Encounter;