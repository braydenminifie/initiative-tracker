import "./Encounter.css";
import { Link } from "react-router-dom";

const Encounter = ({ encounter }) => {
  return (
    <Link
      key = {encounter.id}
      to={`/encounters/${encounter.id}`}
      >
    <div className="encounter-card">

      <div className="encounter-card__content">
        <h2 className="encounter-card__title">
          {encounter.name}
        </h2>

        <p className="encounter-card__turns">
          Turns Played: {encounter.turn}
        </p>
      </div>

    </div>
    </Link>
  );
};

export default Encounter;