import React, { useState } from "react";

function Preferences() {
  const [preferences, setPreferences] = useState("");

  const handleSavePreferences = async () => {
    try {
      const email = localStorage.getItem("email");
      const response = await fetch("http://localhost:5000/api/preferences", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
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
    <div>
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
