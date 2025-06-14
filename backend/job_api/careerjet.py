import requests

def search_careerjet_jobs(title, location=None, salary_min=None):
    endpoint = "https://public.api.careerjet.net/search"
    
    params = {
        "keywords": title,
        "location": location or "",
        "salary_min": salary_min or "",
        "locale_code": "en_US",
        "user_ip": "1.2.3.4",
        "user_agent": "Mozilla/5.0",
        "affid": "your_affid_here",   # ⛳️ Get your affiliate ID
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    # Extract relevant job fields
    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("locations"),
            "url": job.get("url"),
            "description": job.get("description")
        })

    return jobs
import requests

def search_careerjet_jobs(title, location=None, salary_min=None):
    endpoint = "https://public.api.careerjet.net/search"
    
    params = {
        "keywords": title,
        "location": location or "",
        "salary_min": salary_min or "",
        "locale_code": "en_US",
        "user_ip": "1.2.3.4",
        "user_agent": "Mozilla/5.0",
        "affid": "your_affid_here",   # ⛳️ Get your affiliate ID
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    # Extract relevant job fields
    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("locations"),
            "url": job.get("url"),
            "description": job.get("description")
        })

    return jobs
