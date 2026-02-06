"""
LinkedIn Job Application Assistant - Demo & Main Usage
Shows how to use the agent with real-world scenarios
"""

import json
from linkedin_agent import LinkedInAgent, UserProfile, JobPosting
from linkedin_utils import JobPostingParser, ProfileValidator, InterviewSimulator


def demo_basic_analysis():
    """Demo 1: Basic job posting analysis"""
    print("=" * 80)
    print("DEMO 1: Basic Job Posting Analysis")
    print("=" * 80)
    
    # Create user profile
    user = UserProfile(
        name="Sarah Chen",
        current_role="Full Stack Developer",
        years_experience=4,
        skills=[
            "Python", "JavaScript", "React", "Node.js", "SQL", 
            "MongoDB", "Docker", "REST APIs", "Git"
        ],
        previous_roles=["Junior Developer", "Web Developer Intern"],
        education="Bachelor's in Computer Science",
        certifications=["AWS Certified Cloud Practitioner"]
    )
    
    # Job posting
    job = JobPosting(
        title="Senior Full Stack Engineer",
        company="StartupXYZ",
        description="We're looking for a full stack engineer to build scalable web applications...",
        required_skills=["Python", "JavaScript", "React", "Node.js", "SQL"],
        preferred_skills=["Docker", "AWS", "MongoDB", "GraphQL"],
        experience_years=5,
        seniority_level="Senior"
    )
    
    # Analyze
    agent = LinkedInAgent(user)
    analysis = agent.analyze_job_posting(job)
    
    print(f"\nJob: {analysis['job_title']} at {analysis['company']}")
    print(f"Match Score: {analysis['match_score']['percentage']}% - {analysis['match_score']['rating']}")
    print(f"\nRecommendation: {analysis['recommendation']}\n")
    
    print("STRONG POINTS:")
    for point in analysis['strong_points']:
        print(f"  ✓ {point}")
    
    print("\nAREAS TO IMPROVE:")
    for area in analysis['improvement_areas']:
        print(f"  • {area}")
    
    print("\nCOVER LETTER TIPS:")
    for tip in analysis['cover_letter_tips']:
        print(f"  → {tip}")
    
    print("\nINTERVIEW PREP:")
    interview = analysis['interview_preparation']
    print("  Likely Questions:")
    for q in interview['likely_questions']:
        print(f"    - {q}")
    print("  Preparation Tips:")
    for t in interview['preparation_tips']:
        print(f"    - {t}")


def demo_multiple_jobs():
    """Demo 2: Compare multiple job postings"""
    print("\n" + "=" * 80)
    print("DEMO 2: Comparing Multiple Job Opportunities")
    print("=" * 80)
    
    user = UserProfile(
        name="Alex Johnson",
        current_role="Software Engineer",
        years_experience=6,
        skills=[
            "Java", "Python", "Spring Boot", "MongoDB", "AWS", 
            "Docker", "Kubernetes", "CI/CD", "Microservices"
        ],
        previous_roles=["Backend Developer", "Junior Developer"],
        education="BS Computer Science",
        certifications=["AWS Solutions Architect", "Kubernetes Certified"]
    )
    
    jobs = [
        JobPosting(
            title="Backend Engineer",
            company="TechCorp",
            description="Backend engineer needed...",
            required_skills=["Java", "Spring Boot", "SQL"],
            preferred_skills=["Kubernetes", "AWS"],
            experience_years=5,
            seniority_level="Mid"
        ),
        JobPosting(
            title="DevOps Engineer",
            company="CloudFirst Inc",
            description="DevOps specialist needed...",
            required_skills=["Docker", "Kubernetes", "CI/CD", "AWS"],
            preferred_skills=["Terraform", "Prometheus"],
            experience_years=6,
            seniority_level="Senior"
        ),
        JobPosting(
            title="Full Stack Python Developer",
            company="StartupABC",
            description="Full stack Python developer...",
            required_skills=["Python", "Django", "React", "PostgreSQL"],
            preferred_skills=["Docker", "Redis"],
            experience_years=3,
            seniority_level="Mid"
        )
    ]
    
    agent = LinkedInAgent(user)
    
    print(f"\nAnalyzing {len(jobs)} jobs for {user.name}...\n")
    
    results = []
    for job in jobs:
        analysis = agent.analyze_job_posting(job)
        results.append({
            "job": f"{job.title} at {job.company}",
            "score": analysis['match_score']['percentage'],
            "rating": analysis['match_score']['rating']
        })
    
    # Sort by match score
    results.sort(key=lambda x: x['score'], reverse=True)
    
    print("RANKED OPPORTUNITIES:\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['job']}")
        print(f"   Match Score: {result['score']}% ({result['rating']})\n")


def demo_profile_optimization():
    """Demo 3: Profile optimization suggestions"""
    print("\n" + "=" * 80)
    print("DEMO 3: LinkedIn Profile Optimization")
    print("=" * 80)
    
    # Incomplete profile
    weak_profile = UserProfile(
        name="Mike Rodriguez",
        current_role="Developer",
        years_experience=2,
        skills=["Java", "Python"],
        previous_roles=["Intern"],
        education="",
        certifications=[]
    )
    
    # Optimized profile
    strong_profile = UserProfile(
        name="Mike Rodriguez",
        current_role="Senior Software Engineer",
        years_experience=6,
        skills=[
            "Java", "Python", "Spring Boot", "Docker", "AWS", 
            "Kubernetes", "Microservices", "SQL", "REST APIs", "Problem Solving"
        ],
        previous_roles=[
            "Software Engineer",
            "Junior Developer",
            "Intern"
        ],
        education="BS Computer Science, State University",
        certifications=[
            "AWS Solutions Architect",
            "Certified Kubernetes Administrator",
            "Oracle Java Programmer"
        ]
    )
    
    print("\nWEAK PROFILE ANALYSIS:")
    weak_score = ProfileValidator.calculate_profile_completeness(weak_profile)
    print(f"Completeness Score: {weak_score}/100")
    print("Suggestions:")
    for suggestion in ProfileValidator.get_profile_improvement_suggestions(weak_profile):
        print(f"  → {suggestion}")
    
    print("\n" + "-" * 80)
    print("\nSTRONG PROFILE ANALYSIS:")
    strong_score = ProfileValidator.calculate_profile_completeness(strong_profile)
    print(f"Completeness Score: {strong_score}/100")
    
    suggestions = ProfileValidator.get_profile_improvement_suggestions(strong_profile)
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"  → {suggestion}")
    else:
        print("✓ Profile is well-optimized!")


def demo_interview_prep():
    """Demo 4: Interview preparation"""
    print("\n" + "=" * 80)
    print("DEMO 4: Interview Preparation Simulator")
    print("=" * 80)
    
    skills = ["Python", "JavaScript", "React"]
    
    print(f"\nGenerating interview questions based on skills: {', '.join(skills)}\n")
    
    print("TECHNICAL QUESTIONS:")
    for i, question in enumerate(InterviewSimulator.generate_technical_questions(skills), 1):
        print(f"  {i}. {question}")
    
    print("\nBEHAVIORAL QUESTIONS:")
    for i, question in enumerate(InterviewSimulator.generate_behavioral_questions(), 1):
        print(f"  {i}. {question}")


def demo_job_description_parsing():
    """Demo 5: Parse job description text"""
    print("\n" + "=" * 80)
    print("DEMO 5: Job Description Parsing")
    print("=" * 80)
    
    job_description = """
    We are looking for a Senior Full Stack Engineer with 5+ years of experience.
    The ideal candidate should have strong Python and JavaScript skills.
    Experience with React, Node.js, and Docker is required.
    Knowledge of AWS, Kubernetes, and CI/CD practices is a plus.
    You should be familiar with SQL and REST APIs.
    """
    
    print("Job Description:")
    print(job_description)
    
    parsed = JobPostingParser.parse_from_text(job_description)
    
    print("\nPARSED INFORMATION:")
    print(f"Skills Found: {', '.join(sorted(parsed['skills']))}")
    print(f"Experience Required: {parsed['years']}+ years")


def interactive_mode():
    """Interactive mode for real-time analysis"""
    print("\n" + "=" * 80)
    print("INTERACTIVE MODE - Create Your Own Analysis")
    print("=" * 80)
    
    # For demonstration, using predefined profiles
    sample_profiles = {
        "1": UserProfile(
            name="Alice Johnson",
            current_role="Senior Developer",
            years_experience=7,
            skills=["Python", "JavaScript", "React", "Django", "PostgreSQL", "Docker", "AWS"],
            previous_roles=["Developer", "Junior Developer"],
            education="BS Computer Science",
            certifications=["AWS Architect"]
        ),
        "2": UserProfile(
            name="Bob Smith",
            current_role="ML Engineer",
            years_experience=5,
            skills=["Python", "TensorFlow", "PyTorch", "SQL", "Spark"],
            previous_roles=["Data Scientist", "Analyst"],
            education="BS Statistics",
            certifications=[]
        )
    }
    
    sample_jobs = {
        "1": JobPosting(
            title="Full Stack Developer",
            company="Tech Startup",
            description="Looking for full stack developer",
            required_skills=["Python", "React", "PostgreSQL"],
            preferred_skills=["Docker", "AWS"],
            experience_years=5,
            seniority_level="Senior"
        ),
        "2": JobPosting(
            title="Machine Learning Engineer",
            company="AI Corp",
            description="ML engineer for computer vision",
            required_skills=["Python", "TensorFlow", "PyTorch"],
            preferred_skills=["Keras", "OpenCV"],
            experience_years=4,
            seniority_level="Mid"
        )
    }
    
    print("\nAvailable profiles:")
    for key, profile in sample_profiles.items():
        print(f"  {key}. {profile.name} - {profile.current_role}")
    
    print("\nAvailable jobs:")
    for key, job in sample_jobs.items():
        print(f"  {key}. {job.title} at {job.company}")
    
    # Default analysis
    print("\nRunning default analysis: Alice Johnson -> Tech Startup Full Stack Developer")
    agent = LinkedInAgent(sample_profiles["1"])
    analysis = agent.analyze_job_posting(sample_jobs["1"])
    
    print(f"\nResult: {analysis['match_score']['percentage']}% match ({analysis['match_score']['rating']})")
    print(f"Recommendation: {analysis['recommendation']}")


if __name__ == "__main__":
    # Run all demos
    demo_basic_analysis()
    demo_multiple_jobs()
    demo_profile_optimization()
    demo_interview_prep()
    demo_job_description_parsing()
    # interactive_mode()
    
    print("\n" + "=" * 80)
    print("All demos completed! Use the LinkedInAgent class for your own analyses.")
    print("=" * 80)
