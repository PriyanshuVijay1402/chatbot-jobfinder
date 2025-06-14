from fastapi import FastAPI, Query
from parser.query_parser import parse_query
from job_api.careerjet import search_careerjet_jobs
from job_api.jooble import search_jooble_jobs

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Job Finder API is running!"}

@app.get("/search_jobs")
def search_jobs(query: str = Query(..., description="Job search query in plain language")):
    # Parse the user query
    parsed = parse_query(query)
    title = parsed["title"]
    location = parsed["location"]
    salary_min = parsed["salary_min"]

    # Fetch from Careerjet
    cj_jobs = []
    try:
        cj_jobs = search_careerjet_jobs(title, location, salary_min)
    except Exception as e:
        print(f"[Careerjet Error]: {e}")

    # Fetch from Jooble
    jooble_jobs = []
    try:
        jooble_jobs = search_jooble_jobs(title, location, salary_min)
    except Exception as e:
        print(f"[Jooble Error]: {e}")

    # Combine both sources
    return {
        "query": query,
        "parsed": parsed,
        "careerjet_jobs": cj_jobs,
        "jooble_jobs": jooble_jobs
    }
