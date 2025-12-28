def calculate_weighted_score(candidate_skills, job_skills):
    score = 0
    for skill, weight in job_skills.items():
        if skill.lower() in candidate_skills:
            score += weight
    return round(score * 100, 2)
#new one for the resume adding
def get_top_n_jobs(candidate_skills, jobs, top_n=5):
    results = []
    for job in jobs:
        score = calculate_weighted_score(candidate_skills, job["skills"])
        results.append({**job, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]

