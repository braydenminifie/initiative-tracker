import "./EncountersGrid.css";
import Encounter from "./Encounter";

const EncountersGrid = ({ encounters = [], setEncounters }) => {
  /* Delete Encounter */
  async function deleteEncounter(encounterId) {
    const response = await fetch(
      `http://localhost:5000/api/encounters/${encounterId}`,
      {
        method: "DELETE",
      }
    );

    if (!response.ok) {
      throw new Error("Failed to delete encounter");
    }

    return response.json();
  }

  const handleDeleteEncounter = async (encounterId) => {
    try {
      await deleteEncounter(encounterId);
      setEncounters((prev) =>
        prev.filter((encounter) => encounter.id !== encounterId)
      );

    } catch (error) {
      console.error(error);
    }
  };
  
  /* Component */
  return (
    <section className="encounters-grid">
      {encounters.map((encounter) => (
        <Encounter
          key={encounter.id}
          encounter={encounter}
          onDelete={handleDeleteEncounter}
        />
      ))}
    </section>
  );
};

export default EncountersGrid;