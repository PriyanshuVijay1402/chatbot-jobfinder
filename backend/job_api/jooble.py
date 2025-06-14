import requests

def search_jooble_jobs(title, location=None, salary_min=None):
    url = "https://jooble.org/api/a9d18398-68ed-4309-8091-a02c9aca5568"
    body = {
        "keywords": title,
        "location": location or "",
    }

    if salary_min:
        body["salary"] = salary_min

    response = requests.post(url, json=body)
    data = response.json()

    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("location"),
            "url": job.get("link"),
            "description": job.get("snippet")
        })

    return jobs
