import React, { useState, useEffect } from "react";

function NewsSummaries() {
  const [summaries, setSummaries] = useState([]);

  useEffect(() => {
    const fetchSummaries = async () => {
      try {
        const email = localStorage.getItem("email");
        const response = await fetch("http://localhost:5000/api/news", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email }),
        });
        if (response.ok) {
          const data = await response.json();
          setSummaries(data.news_summary);
        } else {
          console.error("Failed to fetch news summaries");
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchSummaries();
  }, []);

  return (
    <div>
      <h2>News Summaries</h2>
      <ul>
        {summaries.map((summary, index) => (
          <li key={index}>{summary}</li>
        ))}
      </ul>
    </div>
  );
}

export default NewsSummaries;
