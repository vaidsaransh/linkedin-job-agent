#!/usr/bin/env python3
"""
Quick Start Guide - LinkedIn Job Application Assistant
Run this file to get started immediately!
"""

from linkedin_agent import LinkedInAgent, UserProfile, JobPosting
from linkedin_utils import ProfileValidator, InterviewSimulator


def main():
    print("\n" + "="*70)
    print("  LINKEDIN JOB APPLICATION ASSISTANT - Quick Start")
    print("="*70 + "\n")
    
    # Step 1: Create Your Profile
    print("STEP 1: Creating your LinkedIn profile...\n")
    
    my_profile = UserProfile(
        name="Sarah Chen",
        current_role="Full Stack Developer",
        years_experience=4,
        skills=[
            "Python", "JavaScript", "React", "Node.js", 
            "SQL", "MongoDB", "Docker", "REST APIs"
        ],
        previous_roles=["Junior Developer", "Web Developer Intern"],
        education="BS Computer Science",
        certifications=["AWS Certified Cloud Practitioner"]
    )
    
    print(f"✓ Profile created for: {my_profile.name}")
    print(f"  Current Role: {my_profile.current_role}")
    print(f"  Experience: {my_profile.years_experience} years")
    print(f"  Skills: {len(my_profile.skills)} total\n")
    
    # Step 2: Check Profile Completeness
    print("STEP 2: Checking your profile completeness...\n")
    
    completeness = ProfileValidator.calculate_profile_completeness(my_profile)
    print(f"✓ Profile Completeness Score: {completeness}/100")
    
    if completeness < 100:
        suggestions = ProfileValidator.get_profile_improvement_suggestions(my_profile)
        if suggestions:
            print("  Suggestions for improvement:")
            for suggestion in suggestions:
                print(f"    • {suggestion}")
    print()
    
    # Step 3: Analyze a Job
    print("STEP 3: Analyzing a job posting...\n")
    
    target_job = JobPosting(
        title="Senior Full Stack Engineer",
        company="TechStartup Inc",
        description="We're looking for an experienced full stack engineer...",
        required_skills=["Python", "JavaScript", "React", "Node.js", "SQL"],
        preferred_skills=["Docker", "AWS", "MongoDB"],
        experience_years=5,
        seniority_level="Senior"
    )
    
    print(f"Job: {target_job.title} at {target_job.company}")
    print(f"Required Skills: {len(target_job.required_skills)}")
    print(f"Preferred Skills: {len(target_job.preferred_skills)}")
    print(f"Experience Required: {target_job.experience_years}+ years\n")
    
    # Step 4: Run Analysis
    print("STEP 4: Running AI analysis...\n")
    
    agent = LinkedInAgent(my_profile)
    analysis = agent.analyze_job_posting(target_job)
    
    # Display Results
    print("="*70)
    print("ANALYSIS RESULTS")
    print("="*70)
    
    print(f"\n📊 MATCH SCORE: {analysis['match_score']['percentage']}%")
    print(f"   Rating: {analysis['match_score']['rating']}\n")
    
    print("💡 RECOMMENDATION:")
    print(f"   {analysis['recommendation']}\n")
    
    print("✅ STRONG POINTS:")
    for point in analysis['strong_points']:
        print(f"   • {point}\n")
    
    print("⚠️  AREAS TO IMPROVE:")
    for area in analysis['improvement_areas']:
        print(f"   • {area}\n")
    
    print("📝 COVER LETTER TALKING POINTS:")
    for tip in analysis['cover_letter_tips']:
        print(f"   • {tip}\n")
    
    print("🎤 INTERVIEW PREPARATION:")
    interview = analysis['interview_preparation']
    print("   Likely Questions:")
    for q in interview['likely_questions'][:2]:
        print(f"     - {q}")
    print("\n   Preparation Tips:")
    for t in interview['preparation_tips'][:2]:
        print(f"     - {t}\n")
    
    # Step 5: Generate Interview Questions
    print("STEP 5: Generating interview prep questions...\n")
    
    top_skills = my_profile.skills[:3]
    print(f"Generating questions for: {', '.join(top_skills)}\n")
    
    tech_questions = InterviewSimulator.generate_technical_questions(top_skills)
    print("TECHNICAL QUESTIONS TO PREPARE FOR:")
    for i, q in enumerate(tech_questions, 1):
        print(f"  {i}. {q}")
    
    print("\n" + "="*70)
    print("✨ You're Ready to Apply!")
    print("="*70)
    print("\nNext Steps:")
    print("  1. Review your strong points above")
    print("  2. Prepare specific examples for interview questions")
    print("  3. Customize your cover letter with talking points")
    print("  4. Craft a compelling subject line in your application")
    print("  5. Practice answering interview questions out loud")
    print("\n📚 For more features:")
    print("  • Run: python demo.py (for comprehensive examples)")
    print("  • Run: python app.py (for web interface)")
    print("  • Check: DOCUMENTATION.md (for detailed guide)\n")


if __name__ == "__main__":
    main()
