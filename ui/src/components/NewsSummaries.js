import React, { useState, useEffect } from "react";
import "../styles/styles.css";

function NewsSummaries() {
  const [summaries, setSummaries] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSummaries = async () => {
      try {
        const email = localStorage.getItem("email");
        const token = localStorage.getItem("token");
        const response = await fetch("http://localhost:5000/api/news", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({ email }),
        });
        if (response.ok) {
          const data = await response.json();
          setSummaries(data.news_summary);
        } else {
          const errorData = await response.json();
          setError(errorData.error || "Failed to fetch news summaries");
        }
      } catch (error) {
        setError("An error occurred. Please try again.");
      }
    };

    fetchSummaries();
  }, []);

  return (
    <div className="container">
      <h2>News Summaries</h2>
      {error ? (
        <p className="error">{error}</p>
      ) : (
        <ul>
          {summaries.map((summary, index) => (
            <li key={index}>{summary}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default NewsSummaries;
