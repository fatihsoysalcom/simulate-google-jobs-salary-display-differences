# This script simulates how job platforms like Google Jobs might display salary information
# differently across various markets, reflecting the article's analysis of transparency.

jobs_data = [
    {
        "title": "Software Engineer",
        "country": "USA",
        "salary_range": "$120,000 - $150,000 annually"
    },
    {
        "title": "Data Scientist",
        "country": "UK",
        "salary_range": "£60,000 - £80,000 per year"
    },
    {
        "title": "Frontend Developer",
        "country": "Canada",
        "salary_range": None # Salary not disclosed for this posting
    },
    {
        "title": "DevOps Engineer",
        "country": "Australia",
        "salary_range": "$100,000 - $130,000 AUD annually"
    },
    {
        "title": "QA Tester",
        "country": "India",
        "salary_range": None # Salary not disclosed for this posting
    },
    {
        "title": "Product Manager",
        "country": "Singapore",
        "salary_range": "SGD 8,000 - 12,000 per month" # Singapore often has monthly salaries
    },
    {
        "title": "Cloud Architect",
        "country": "USA",
        "salary_range": "$160,000 - $200,000 annually"
    },
    {
        "title": "UX Designer",
        "country": "Singapore",
        "salary_range": None # Singapore, but no salary provided for this specific job
    },
    {
        "title": "Marketing Specialist",
        "country": "Canada",
        "salary_range": "CAD 70,000 - 90,000 per year"
    }
]

def display_job_posting(job):
    """Simulates displaying a job posting with market-specific salary transparency rules."""
    print(f"\n--- Job Posting ---")
    print(f"Title: {job['title']}")
    print(f"Country: {job['country']}")

    salary_info = job['salary_range']

    # Simulate different salary disclosure practices based on country
    if job['country'] == "Singapore":
        # Article highlights Singapore's unique approach; simulate more direct disclosure
        if salary_info:
            print(f"Salary: {salary_info} (Singapore market practice)")
        else:
            print("Salary: Disclosed upon interview (Common in Singapore if not specified)")
    elif job['country'] in ["USA", "UK", "Australia"]:
        # These markets often have higher salary transparency, but not always mandatory
        if salary_info:
            print(f"Salary: {salary_info}")
        else:
            print("Salary: Not specified, typically competitive (Common practice)")
    elif job['country'] in ["Canada", "India"]:
        # These markets might have less consistent salary disclosure
        if salary_info:
            print(f"Salary: {salary_info}")
        else:
            print("Salary: Negotiable / Industry standard (Less transparency)")
    else:
        # Default for any other country
        if salary_info:
            print(f"Salary: {salary_info}")
        else:
            print("Salary: Not specified")

# Iterate through the simulated job data and display each posting
for job in jobs_data:
    display_job_posting(job)
