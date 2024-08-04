import React, { useState, useEffect } from "react";
import { fetchNewsSummaries } from "../services/api";
import "./styles/NewsSummaries.css";  // Import component-specific styles

function NewsSummaries() {
  // State for news summaries and error message
  const [summaries, setSummaries] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  // Fetch news summaries on component mount
  useEffect(() => {
    const getSummaries = async () => {
      try {
        setLoading(true);
        const email = localStorage.getItem("email");
        const data = await fetchNewsSummaries(email);
        setSummaries(data.news_summary);
      } catch (error) {
        setError("Failed to fetch news summaries. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    getSummaries();
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
      {loading ? (
        <p>Loading news summaries...</p>
      ) : error ? (
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
