import React, { useState } from "react";
import axios from "axios";
import JobResults from "./JobResults";

const App = () => {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/search_jobs`, {
        params: { query },
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error fetching jobs:", error);
      setResult({ error: "Failed to fetch jobs." });
    }
  };

  return (
    <div className="container">
      <h1>Job Finder Chatbot</h1>
      <input
        type="text"
        placeholder="e.g. Data Scientist in Bangalore with 15L salary"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>

      {result && <JobResults result={result} />}
    </div>
  );
};

export default App;
