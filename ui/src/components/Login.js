import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { loginUser } from "../services/api";
import "./styles/Login.css";  // Import component-specific styles
import { Link } from "react-router-dom";


function Login() {
  // State for email input and error message
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const history = useHistory();

  // Handle login form submission
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const data = await loginUser(email);
      // Store token and email in localStorage
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("email", email);
      // Redirect to preferences page
      history.push("/preferences");
    } catch (error) {
      setError("Login failed. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
      <p>
        Don't have an account? <Link to="/register">Register here</Link>
      </p>
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default Login;
