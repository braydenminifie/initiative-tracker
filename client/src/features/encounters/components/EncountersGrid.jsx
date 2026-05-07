import "./EncountersGrid.css";
import Encounter from "./Encounter";

const EncountersGrid = ({ encounters = [] }) => {
  return (
    <section className="encounters-grid">
      {encounters.map((encounter) => (
        <Encounter
          key={encounter.id}
          encounter={encounter}
        />
      ))}
    </section>
  );
};

export default EncountersGrid;