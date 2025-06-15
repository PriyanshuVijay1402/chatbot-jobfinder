import React from "react";

const JobResults = ({ result }) => {
  const renderJobs = (jobs, source) => (
    <div>
      <h3>{source} Jobs:</h3>
      {jobs.length === 0 ? (
        <p>No jobs found.</p>
      ) : (
        jobs.map((job, index) => (
          <div className="job-card" key={index}>
            <h4>{job.title}</h4>
            <p><strong>Company:</strong> {job.company}</p>
            <p><strong>Location:</strong> {job.location}</p>
            <a href={job.url} target="_blank" rel="noreferrer">View Job</a>
          </div>
        ))
      )}
    </div>
  );

  return (
    <div>
      <h2>Query: {result.query}</h2>
      {renderJobs(result.careerjet_jobs, "Careerjet")}
      {renderJobs(result.jooble_jobs, "Jooble")}
    </div>
  );
};

export default JobResults;
