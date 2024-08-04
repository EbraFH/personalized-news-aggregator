import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { savePreferences } from "../services/api";
import "./styles/Preferences.css";  // Import component-specific styles


function Preferences() {
  // State for preferences input and error message
  const [preferences, setPreferences] = useState("");
  const [error, setError] = useState("");
  const history = useHistory();

  // Handle save preferences form submission
  const handleSavePreferences = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      const email = localStorage.getItem("email");
      await savePreferences(email, preferences.split(","), token);
      // Redirect to news page after saving preferences
      history.push("/news");
    } catch (error) {
      setError("Failed to save preferences. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Set Preferences</h2>
      <form onSubmit={handleSavePreferences}>
        <input
          type="text"
          placeholder="Enter your preferences (comma separated)"
          value={preferences}
          onChange={(e) => setPreferences(e.target.value)}
          required
        />
        <button type="submit">Save Preferences</button>
      </form>
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default Preferences;
