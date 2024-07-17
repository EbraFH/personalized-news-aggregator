import React, { useState } from "react";
import "./styles/Register.css";

function Register() {
  const [email, setEmail] = useState("");
  const [preferences, setPreferences] = useState("");
  const [message, setMessage] = useState("");

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
        setMessage(`Registration successful! User ID: ${data.user_id}`);
        window.location.href = "/login";
      } else {
        const errorData = await response.json();
        setMessage(`Registration failed: ${errorData.error}`);
      }
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    }
  };

  return (
    <div className="container">
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
      {message && <p>{message}</p>}
    </div>
  );
}

export default Register;
