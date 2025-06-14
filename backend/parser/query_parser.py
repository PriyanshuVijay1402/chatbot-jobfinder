import re

def parse_query(query):
    result = {
        "title": None,
        "location": None,
        "salary_min": None
    }

    # Extract salary like: "salary more than 100K" or "salary above 80000"
    salary_match = re.search(r"salary.*?(?:more than|above)?\s?(\d+)[kK]?", query, re.IGNORECASE)
    if salary_match:
        result["salary_min"] = int(salary_match.group(1)) * 1000

    # Extract location if present using "in [Location]"
    loc_match = re.search(r"in ([A-Za-z\s]+?)(?: with|$)", query, re.IGNORECASE)
    if loc_match:
        result["location"] = loc_match.group(1).strip().title()

    # Extract job title before "in", "with", or end
    title_match = re.split(r"\s(?:in|with|salary)\s", query, flags=re.IGNORECASE)
    if title_match:
        result["title"] = title_match[0].strip().title()

    return result
