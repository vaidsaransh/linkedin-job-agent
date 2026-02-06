"""
Example Profiles and Job Postings for Testing
Use these as templates for your own profiles
"""

from linkedin_agent import UserProfile, JobPosting

# ============================================================================
# EXAMPLE USER PROFILES
# ============================================================================

# Profile 1: Frontend Developer
FRONTEND_DEVELOPER = UserProfile(
    name="Emily Rodriguez",
    current_role="Frontend Developer",
    years_experience=3,
    skills=[
        "JavaScript", "React", "Vue.js", "CSS", "HTML", 
        "Webpack", "Jest", "Git", "REST APIs", "Responsive Design"
    ],
    previous_roles=["Junior Frontend Developer", "Web Developer Intern"],
    education="BS Computer Science, UC Berkeley",
    certifications=["Google Cloud Associate Cloud Engineer"]
)

# Profile 2: Backend/DevOps Engineer
BACKEND_DEVOPS = UserProfile(
    name="Alex Kim",
    current_role="Backend Engineer",
    years_experience=6,
    skills=[
        "Python", "Java", "Spring Boot", "Docker", "Kubernetes",
        "AWS", "PostgreSQL", "MongoDB", "CI/CD", "Terraform"
    ],
    previous_roles=["Junior Backend Developer", "Systems Admin Intern"],
    education="BS Information Technology, Carnegie Mellon",
    certifications=["AWS Solutions Architect", "Certified Kubernetes Administrator"]
)

# Profile 3: Data Science
DATA_SCIENTIST = UserProfile(
    name="Nina Patel",
    current_role="Data Scientist",
    years_experience=5,
    skills=[
        "Python", "SQL", "TensorFlow", "PyTorch", "Pandas",
        "Scikit-learn", "Apache Spark", "Tableau", "A/B Testing", "Statistics"
    ],
    previous_roles=["Junior Data Scientist", "Data Analyst"],
    education="MS Data Science, Stanford",
    certifications=["AWS Machine Learning Specialty", "Google Cloud Data Engineer"]
)

# Profile 4: Full Stack Developer (Mid-level)
FULL_STACK_MID = UserProfile(
    name="James Wilson",
    current_role="Full Stack Developer",
    years_experience=5,
    skills=[
        "Python", "JavaScript", "React", "Node.js", "Express",
        "SQL", "MongoDB", "Docker", "AWS", "Git", "REST APIs"
    ],
    previous_roles=["Frontend Developer", "Intern"],
    education="BS Computer Science",
    certifications=["AWS Solutions Architect Associate"]
)

# Profile 5: Junior Developer (Entry-level)
JUNIOR_DEVELOPER = UserProfile(
    name="Sophie Johnson",
    current_role="Junior Software Developer",
    years_experience=1,
    skills=[
        "Python", "JavaScript", "React", "HTML", "CSS",
        "Git", "Problem Solving", "SQL", "API Development"
    ],
    previous_roles=["Bootcamp Graduate", "Intern"],
    education="Coding Bootcamp Graduate",
    certifications=[]
)


# ============================================================================
# EXAMPLE JOB POSTINGS
# ============================================================================

# Job 1: Senior Full Stack Engineer
JOB_SENIOR_FULLSTACK = JobPosting(
    title="Senior Full Stack Engineer",
    company="TechCorp Inc",
    description="""
    We're looking for an experienced full stack engineer to lead our platform development.
    You'll work with cutting-edge technologies and mentor junior developers.
    Strong problem-solving skills and 5+ years of experience required.
    """,
    required_skills=["Python", "JavaScript", "React", "Node.js", "SQL", "Docker"],
    preferred_skills=["AWS", "Kubernetes", "MongoDB", "GraphQL", "RedisCache"],
    experience_years=5,
    seniority_level="Senior"
)

# Job 2: Frontend Engineer
JOB_FRONTEND = JobPosting(
    title="Frontend Engineer",
    company="StartupXYZ",
    description="""
    Join our growing team and build beautiful user interfaces.
    You'll be responsible for creating responsive and interactive web applications.
    Experience with modern React ecosystem is essential.
    """,
    required_skills=["JavaScript", "React", "CSS", "HTML", "Git"],
    preferred_skills=["TypeScript", "Redux", "Testing", "Webpack"],
    experience_years=2,
    seniority_level="Mid"
)

# Job 3: Backend Engineer
JOB_BACKEND = JobPosting(
    title="Backend Engineer",
    company="CloudServices Ltd",
    description="""
    Build scalable backend services for millions of users.
    Work with cloud infrastructure and microservices architecture.
    Expertise in backend technologies and database optimization required.
    """,
    required_skills=["Python", "Java", "PostgreSQL", "Docker", "AWS"],
    preferred_skills=["Spring Boot", "Kubernetes", "Redis", "Message Queues"],
    experience_years=4,
    seniority_level="Senior"
)

# Job 4: DevOps Engineer
JOB_DEVOPS = JobPosting(
    title="DevOps Engineer",
    company="InfraCorp",
    description="""
    Manage and optimize our cloud infrastructure using modern DevOps practices.
    Implement CI/CD pipelines and ensure system reliability.
    Strong knowledge of container orchestration and infrastructure as code required.
    """,
    required_skills=["Docker", "Kubernetes", "AWS", "CI/CD", "Terraform"],
    preferred_skills=["Python", "Prometheus", "ELK Stack", "Helm"],
    experience_years=5,
    seniority_level="Senior"
)

# Job 5: Data Scientist
JOB_DATA_SCIENTIST = JobPosting(
    title="Machine Learning Engineer",
    company="AI Solutions",
    description="""
    Develop and deploy machine learning models that power our platform.
    Work with large datasets and optimize model performance.
    Experience with deep learning frameworks and statistical analysis required.
    """,
    required_skills=["Python", "TensorFlow", "SQL", "Statistics", "Pandas"],
    preferred_skills=["PyTorch", "Scikit-learn", "AWS SageMaker", "Spark"],
    experience_years=3,
    seniority_level="Mid"
)

# Job 6: Junior Developer
JOB_JUNIOR = JobPosting(
    title="Junior Software Developer",
    company="Learning Lab",
    description="""
    Start your tech career with us! We're looking for enthusiastic junior developers.
    Great for recent bootcamp graduates or early-career developers.
    We provide mentorship and a supportive learning environment.
    """,
    required_skills=["Python", "JavaScript", "HTML", "CSS", "Git"],
    preferred_skills=["React", "Database Design", "Problem Solving"],
    experience_years=0,
    seniority_level="Entry"
)

# Job 7: Data Analyst
JOB_DATA_ANALYST = JobPosting(
    title="Data Analyst",
    company="Analytics Pro",
    description="""
    Transform raw data into actionable insights.
    Work with SQL, create dashboards, and support decision-making.
    Strong analytical skills and attention to detail required.
    """,
    required_skills=["SQL", "Excel", "Tableau", "Statistics"],
    preferred_skills=["Python", "Power BI", "A/B Testing", "Python"],
    experience_years=2,
    seniority_level="Mid"
)


# ============================================================================
# MATCHING SCENARIOS (Profile -> Job pairs)
# ============================================================================

SCENARIOS = {
    "perfect_match": {
        "profile": FULL_STACK_MID,
        "job": JOB_SENIOR_FULLSTACK,
        "description": "Nearly perfect match - has most skills, slightly short on experience"
    },
    "good_fit": {
        "profile": FRONTEND_DEVELOPER,
        "job": JOB_FRONTEND,
        "description": "Good match - aligned experience and skills"
    },
    "career_pivot": {
        "profile": JUNIOR_DEVELOPER,
        "job": JOB_JUNIOR,
        "description": "Entry-level match - perfect starting point"
    },
    "specialization_needed": {
        "profile": FRONTEND_DEVELOPER,
        "job": JOB_DEVOPS,
        "description": "Challenging - requires significant skill development"
    },
    "recent_grad": {
        "profile": JUNIOR_DEVELOPER,
        "job": JOB_FRONTEND,
        "description": "Good fit - some overlap but gaps exist"
    },
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_all_profiles():
    """Return all example profiles"""
    return {
        "frontend": FRONTEND_DEVELOPER,
        "backend": BACKEND_DEVOPS,
        "data_scientist": DATA_SCIENTIST,
        "fullstack": FULL_STACK_MID,
        "junior": JUNIOR_DEVELOPER
    }


def get_all_jobs():
    """Return all example job postings"""
    return {
        "senior_fullstack": JOB_SENIOR_FULLSTACK,
        "frontend": JOB_FRONTEND,
        "backend": JOB_BACKEND,
        "devops": JOB_DEVOPS,
        "data_scientist": JOB_DATA_SCIENTIST,
        "junior": JOB_JUNIOR,
        "data_analyst": JOB_DATA_ANALYST
    }


def get_scenario(scenario_name):
    """Get a specific matching scenario"""
    return SCENARIOS.get(scenario_name)


if __name__ == "__main__":
    # Print available examples
    print("\n=== AVAILABLE PROFILES ===")
    for key, profile in get_all_profiles().items():
        print(f"  {key}: {profile.name} ({profile.current_role})")
    
    print("\n=== AVAILABLE JOBS ===")
    for key, job in get_all_jobs().items():
        print(f"  {key}: {job.title} at {job.company}")
    
    print("\n=== MATCHING SCENARIOS ===")
    for key, scenario in SCENARIOS.items():
        print(f"  {key}: {scenario['description']}")
