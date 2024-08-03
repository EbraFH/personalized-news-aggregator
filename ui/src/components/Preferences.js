import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import "../styles/styles.css";

function Preferences() {
  const [preferences, setPreferences] = useState("");
  const [error, setError] = useState("");
  const history = useHistory();

  const handleSavePreferences = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      const email = localStorage.getItem("email");
      const response = await fetch("http://localhost:5000/api/preferences", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          email,
          preferences: preferences.split(",").map((p) => p.trim()),
        }),
      });
      if (response.ok) {
        history.push("/news");
      } else {
        const errorData = await response.json();
        setError(errorData.error || "Failed to save preferences");
      }
    } catch (error) {
      setError("An error occurred. Please try again.");
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
