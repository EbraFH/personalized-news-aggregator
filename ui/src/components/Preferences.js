import React, { useState } from "react";
import "./styles/Preferences.css";

function Preferences() {
  const [preferences, setPreferences] = useState("");

  const handleSavePreferences = async () => {
    try {
      const token = localStorage.getItem("token");
      const email = localStorage.getItem("email");
      const response = await fetch("http://localhost:5000/api/preferences", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ email, preferences: preferences.split(",") }),
      });
      if (response.ok) {
        window.location.href = "/news";
      } else {
        console.error("Failed to save preferences");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="container">
      <h2>Set Preferences</h2>
      <input
        type="text"
        placeholder="Enter your preferences (comma separated)"
        value={preferences}
        onChange={(e) => setPreferences(e.target.value)}
      />
      <button onClick={handleSavePreferences}>Save Preferences</button>
    </div>
  );
}

export default Preferences;
