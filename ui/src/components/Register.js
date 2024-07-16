import React, { useState } from "react";

function Register() {
  const [email, setEmail] = useState("");
  const [preferences, setPreferences] = useState("");

  const handleRegister = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, preferences: preferences.split(",") }),
      });
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem("email", email);
        // Redirect to login page after successful registration
        window.location.href = "/login";
      } else {
        console.error("Registration failed");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="text"
        placeholder="Enter your preferences (comma separated)"
        value={preferences}
        onChange={(e) => setPreferences(e.target.value)}
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
