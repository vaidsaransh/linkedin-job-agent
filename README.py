"""
LinkedIn Job Application Assistant

A unique AI agent that solves the real-world problem of job hunting inefficiency.
Helps job seekers:
- Analyze job postings
- Match skills against requirements  
- Get personalized application strategies
- Prepare for interviews
- Optimize LinkedIn profiles

FEATURES:
1. Job Posting Analysis - Get detailed match scores and recommendations
2. Skill Matching - Identify what you have, what you're missing
3. Interview Preparation - Targeted questions based on job requirements
4. Profile Optimization - Guided profile improvements
5. Application Strategy - Personalized tips for better applications

REAL-WORLD PROBLEM SOLVED:
Most job seekers apply to jobs without understanding:
- How well they actually match
- What skills they're missing
- How to position themselves
- What to expect in interviews

This agent provides data-driven insights to make informed decisions.

USAGE:

1. INSTALL DEPENDENCIES:
   pip install -r requirements.txt

2. RUN COMMAND LINE DEMO:
   python demo.py

3. RUN WEB INTERFACE:
   python app.py
   Then open http://localhost:5000

4. PROGRAMMATIC USE:
   from linkedin_agent import LinkedInAgent, UserProfile, JobPosting
   
   # Create profile
   profile = UserProfile(
       name="John Doe",
       current_role="Developer",
       years_experience=5,
       skills=["Python", "React", "AWS"],
       previous_roles=["Junior Dev"],
       education="BS CS",
       certifications=[]
   )
   
   # Create job posting
   job = JobPosting(
       title="Senior Developer",
       company="TechCorp",
       description="...",
       required_skills=["Python", "React"],
       preferred_skills=["AWS", "Docker"],
       experience_years=5,
       seniority_level="Senior"
   )
   
   # Analyze
   agent = LinkedInAgent(profile)
   analysis = agent.analyze_job_posting(job)
   print(analysis)

FILES:
- linkedin_agent.py: Core agent logic and matching algorithms
- linkedin_utils.py: Utility functions (parsing, validation, tracking)
- demo.py: Comprehensive command-line demonstrations
- app.py: Flask web interface for easy interaction
- requirements.txt: Python dependencies

COMPONENTS:
1. JobMatcher - Matches user skills against job requirements
2. ApplicationAdvisor - Generates personalized tips and strategies
3. LinkedInAgent - Main orchestrator
4. ProfileValidator - Scores and improves profiles
5. InterviewSimulator - Generates interview questions
6. JobPostingParser - Extracts info from job descriptions

WHY IT'S USEFUL:
- Data-driven instead of guesswork
- Saves time applying to bad-fit jobs
- Identifies learning priorities
- Boosts confidence with preparation
- Increases interview success rates
"""

__version__ = "1.0.0"
__author__ = "LinkedIn Assistant Dev"
