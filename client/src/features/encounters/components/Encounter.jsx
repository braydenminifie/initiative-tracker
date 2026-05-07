import "./Encounter.css";

const Encounter = ({ encounter }) => {
  return (
    <div className="encounter-card">

      <div className="encounter-card__content">
        <h2 className="encounter-card__title">
          {encounter.name}
        </h2>

        <p className="encounter-card__turns">
          Turns Played: {encounter.turnsPlayed}
        </p>
      </div>

    </div>
  );
};

export default Encounter;