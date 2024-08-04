import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { registerUser } from "../services/api";
import "./styles/Register.css";  // Import component-specific styles


function Register() {
  // State for email, preferences, and message
  const [email, setEmail] = useState("");
  const [preferences, setPreferences] = useState("");
  const [message, setMessage] = useState("");
  const history = useHistory();

  // Handle register form submission
  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const data = await registerUser(email, preferences.split(","));
      setMessage(`Registration successful! User ID: ${data.user_id}`);
      // Redirect to login page after successful registration
      setTimeout(() => history.push("/login"), 2000);
    } catch (error) {
      setMessage(`Registration failed: ${error.message}`);
    }
  };

  return (
    <div className="container">
      <h2>Register</h2>
      <form onSubmit={handleRegister}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Enter your preferences (comma separated)"
          value={preferences}
          onChange={(e) => setPreferences(e.target.value)}
          required
        />
        <button type="submit">Register</button>
      </form>
      {message && (
        <p className={message.includes("successful") ? "success" : "error"}>
          {message}
        </p>
      )}
    </div>
  );
}

export default Register;
