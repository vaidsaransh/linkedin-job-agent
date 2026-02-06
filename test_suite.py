"""
Comprehensive Test Suite for LinkedIn Job Application Assistant
Tests all features and edge cases
"""

from linkedin_agent import LinkedInAgent, UserProfile, JobPosting
from linkedin_utils import JobPostingParser, ProfileValidator, ApplicationTracker
from examples import get_all_profiles, get_all_jobs, SCENARIOS


def test_basic_matching():
    """Test basic skill matching"""
    print("\n" + "="*70)
    print("TEST 1: Basic Skill Matching")
    print("="*70)
    
    profile = UserProfile(
        name="Test User",
        current_role="Developer",
        years_experience=5,
        skills=["Python", "JavaScript", "React"],
        previous_roles=["Junior Dev"],
        education="BS CS",
        certifications=[]
    )
    
    job = JobPosting(
        title="Senior Python Developer",
        company="TestCorp",
        description="Python development role",
        required_skills=["Python", "JavaScript"],
        preferred_skills=["React", "Docker"],
        experience_years=5,
        seniority_level="Senior"
    )
    
    agent = LinkedInAgent(profile)
    analysis = agent.analyze_job_posting(job)
    
    assert analysis['match_score']['percentage'] >= 80, "Expected high match score"
    print("✓ PASS: Basic matching works correctly")
    print(f"  Match Score: {analysis['match_score']['percentage']}%")


def test_score_calculation():
    """Test match score calculation edge cases"""
    print("\n" + "="*70)
    print("TEST 2: Score Calculation Edge Cases")
    print("="*70)
    
    # Test 1: Perfect match
    profile1 = UserProfile(
        name="Perfect Match", current_role="Dev", years_experience=10,
        skills=["Python", "Java", "SQL"], previous_roles=[], education="BS",
        certifications=[]
    )
    job1 = JobPosting(
        title="Dev", company="C", description="",
        required_skills=["Python", "Java"], preferred_skills=[],
        experience_years=5, seniority_level="Senior"
    )
    agent = LinkedInAgent(profile1)
    score1 = agent.analyze_job_posting(job1)['match_score']['percentage']
    assert score1 >= 90, f"Perfect match should score high, got {score1}"
    print(f"✓ Perfect Match Score: {score1}%")
    
    # Test 2: No matching skills
    profile2 = UserProfile(
        name="No Match", current_role="Dev", years_experience=1,
        skills=["COBOL", "Fortran"], previous_roles=[], education="BS",
        certifications=[]
    )
    job2 = JobPosting(
        title="Python Dev", company="C", description="",
        required_skills=["Python", "JavaScript"], preferred_skills=[],
        experience_years=5, seniority_level="Senior"
    )
    agent = LinkedInAgent(profile2)
    score2 = agent.analyze_job_posting(job2)['match_score']['percentage']
    assert score2 < 50, f"No match should score low, got {score2}"
    print(f"✓ No Match Score: {score2}%")
    
    # Test 3: Experience adjustment
    profile3 = UserProfile(
        name="Junior", current_role="Dev", years_experience=2,
        skills=["Python"], previous_roles=[], education="BS",
        certifications=[]
    )
    job3 = JobPosting(
        title="Python Dev", company="C", description="",
        required_skills=["Python"], preferred_skills=[],
        experience_years=1, seniority_level="Junior"
    )
    agent = LinkedInAgent(profile3)
    score3 = agent.analyze_job_posting(job3)['match_score']['percentage']
    print(f"✓ Experience Adjustment Score: {score3}%")


def test_profile_validation():
    """Test profile validation and completeness scoring"""
    print("\n" + "="*70)
    print("TEST 3: Profile Validation")
    print("="*70)
    
    profiles = get_all_profiles()
    
    for name, profile in profiles.items():
        score = ProfileValidator.calculate_profile_completeness(profile)
        suggestions = ProfileValidator.get_profile_improvement_suggestions(profile)
        
        assert 0 <= score <= 100, f"Score should be 0-100, got {score}"
        print(f"✓ {profile.name}: {score}/100")
        
        if suggestions:
            print(f"  Suggestions: {len(suggestions)} found")


def test_all_job_matches():
    """Test matching all profiles against all jobs"""
    print("\n" + "="*70)
    print("TEST 4: Full Profile-Job Matrix")
    print("="*70)
    
    profiles = get_all_profiles()
    jobs = get_all_jobs()
    
    results = {}
    
    for prof_name, profile in profiles.items():
        agent = LinkedInAgent(profile)
        results[prof_name] = {}
        
        for job_name, job in jobs.items():
            analysis = agent.analyze_job_posting(job)
            score = analysis['match_score']['percentage']
            results[prof_name][job_name] = score
    
    # Find best matches
    print("\nBest Matches Per Profile:")
    for prof_name, matches in results.items():
        best_job = max(matches.items(), key=lambda x: x[1])
        print(f"  {prof_name}: {best_job[0]} ({best_job[1]}%)")


def test_predefined_scenarios():
    """Test predefined matching scenarios"""
    print("\n" + "="*70)
    print("TEST 5: Predefined Scenarios")
    print("="*70)
    
    for scenario_name, scenario in SCENARIOS.items():
        profile = scenario['profile']
        job = scenario['job']
        description = scenario['description']
        
        agent = LinkedInAgent(profile)
        analysis = agent.analyze_job_posting(job)
        score = analysis['match_score']['percentage']
        rating = analysis['match_score']['rating']
        
        print(f"✓ {scenario_name}:")
        print(f"  Description: {description}")
        print(f"  Score: {score}% ({rating})\n")


def test_job_parsing():
    """Test job description parsing"""
    print("\n" + "="*70)
    print("TEST 6: Job Description Parsing")
    print("="*70)
    
    descriptions = [
        "Looking for Python and JavaScript expert with 5+ years",
        "React developer needed. Experience with TypeScript preferred.",
        "DevOps engineer: Docker, Kubernetes, AWS, Terraform"
    ]
    
    for desc in descriptions:
        parsed = JobPostingParser.parse_from_text(desc)
        print(f"Description: {desc}")
        print(f"  Skills found: {len(parsed['skills'])}")
        print(f"  Experience: {parsed['years']}+ years\n")


def test_rating_system():
    """Test the rating system at different score levels"""
    print("\n" + "="*70)
    print("TEST 7: Rating System")
    print("="*70)
    
    test_scores = [95, 75, 55, 25]
    
    agent = LinkedInAgent(UserProfile(
        name="Test", current_role="Dev", years_experience=5,
        skills=["Test"], previous_roles=[], education="",
        certifications=[]
    ))
    
    for score in test_scores:
        rating = agent._rate_match(score)
        print(f"✓ Score {score}% → Rating: {rating}")


def test_application_tracker():
    """Test application history tracking"""
    print("\n" + "="*70)
    print("TEST 8: Application Tracking")
    print("="*70)
    
    tracker = ApplicationTracker()
    
    # Log some applications
    jobs = list(get_all_jobs().values())
    
    tracker.log_application(jobs[0], 85, applied=True)
    tracker.log_application(jobs[1], 70, applied=True)
    tracker.log_application(jobs[2], 45, applied=False)
    tracker.log_application(jobs[3], 60, applied=True)
    
    pattern = tracker.get_success_pattern()
    
    print(f"Total analyzed: {pattern['total_applications']}")
    print(f"Applied: {pattern['applied_count']}")
    print(f"Avg score (applied): {pattern['average_match_score_applied']}%")
    print(f"Avg score (all): {pattern['average_match_score_all']}%")


def run_all_tests():
    """Run all tests"""
    print("\n" + "🧪 " + "="*66 + " 🧪")
    print("  LINKEDIN AGENT - COMPREHENSIVE TEST SUITE")
    print("🧪 " + "="*66 + " 🧪")
    
    try:
        test_basic_matching()
        test_score_calculation()
        test_profile_validation()
        test_all_job_matches()
        test_predefined_scenarios()
        test_job_parsing()
        test_rating_system()
        test_application_tracker()
        
        print("\n" + "="*70)
        print("✅ ALL TESTS PASSED!")
        print("="*70)
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
