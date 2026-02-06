"""
LinkedIn Job Application Assistant Agent
Analyzes job postings and generates personalized application strategies
"""

import json
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum


class SkillMatch(Enum):
    EXPERT = "expert"
    INTERMEDIATE = "intermediate"
    BEGINNER = "beginner"
    NOT_LISTED = "not_listed"


@dataclass
class UserProfile:
    """User's LinkedIn profile data"""
    name: str
    current_role: str
    years_experience: int
    skills: List[str]
    previous_roles: List[str]
    education: str
    certifications: List[str]


@dataclass
class JobPosting:
    """Job posting data"""
    title: str
    company: str
    description: str
    required_skills: List[str]
    preferred_skills: List[str]
    experience_years: int
    seniority_level: str


class JobMatcher:
    """Core matching logic for job applications"""
    
    def __init__(self, user_profile: UserProfile):
        self.user_profile = user_profile
    
    def extract_skill_requirements(self, job_posting: JobPosting) -> Dict[str, List[str]]:
        """Extract and categorize skills from job posting"""
        return {
            "required": job_posting.required_skills,
            "preferred": job_posting.preferred_skills,
            "all": list(set(job_posting.required_skills + job_posting.preferred_skills))
        }
    
    def match_skills(self, job_posting: JobPosting) -> Dict[str, any]:
        """Match user skills against job requirements"""
        skills_required = self.extract_skill_requirements(job_posting)
        user_skills_lower = [s.lower() for s in self.user_profile.skills]
        
        matched = {
            "matched_required": [],
            "matched_preferred": [],
            "missing_required": [],
            "missing_preferred": []
        }
        
        for skill in skills_required["required"]:
            if skill.lower() in user_skills_lower:
                matched["matched_required"].append(skill)
            else:
                matched["missing_required"].append(skill)
        
        for skill in skills_required["preferred"]:
            if skill.lower() in user_skills_lower:
                matched["matched_preferred"].append(skill)
            else:
                matched["missing_preferred"].append(skill)
        
        return matched
    
    def calculate_match_score(self, job_posting: JobPosting) -> float:
        """Calculate overall match percentage (0-100)"""
        skill_match = self.match_skills(job_posting)
        
        required_skills = len(skill_match["matched_required"]) + len(skill_match["missing_required"])
        if required_skills == 0:
            return 0.0
        
        matched_percentage = (len(skill_match["matched_required"]) / required_skills) * 100
        
        # Experience level adjustment
        if self.user_profile.years_experience >= job_posting.experience_years:
            experience_bonus = 10
        else:
            experience_penalty = (job_posting.experience_years - self.user_profile.years_experience) * 5
            experience_bonus = -experience_penalty
        
        final_score = min(100, max(0, matched_percentage + experience_bonus))
        return final_score


class ApplicationAdvisor:
    """Generates application strategies and advice"""
    
    def __init__(self, matcher: JobMatcher, job_posting: JobPosting):
        self.matcher = matcher
        self.job_posting = job_posting
    
    def generate_strong_points(self) -> List[str]:
        """Identify strongest selling points for the application"""
        skill_match = self.matcher.match_skills(self.job_posting)
        
        strong_points = []
        
        # Strong point: Matched required skills
        if skill_match["matched_required"]:
            strong_points.append(
                f"You have {len(skill_match['matched_required'])} of the required skills: "
                f"{', '.join(skill_match['matched_required'][:3])}"
            )
        
        # Strong point: Experience level
        if self.matcher.user_profile.years_experience > self.job_posting.experience_years:
            extra_years = self.matcher.user_profile.years_experience - self.job_posting.experience_years
            strong_points.append(
                f"You have {extra_years} more years of experience than required "
                f"({self.matcher.user_profile.years_experience} vs {self.job_posting.experience_years} required)"
            )
        
        # Strong point: Relevant previous roles
        relevant_roles = [role for role in self.matcher.user_profile.previous_roles 
                         if self.job_posting.title.split()[0].lower() in role.lower()]
        if relevant_roles:
            strong_points.append(f"Previous experience in similar role: {relevant_roles[0]}")
        
        return strong_points
    
    def generate_improvement_areas(self) -> List[str]:
        """Identify areas to improve for better application"""
        skill_match = self.matcher.match_skills(self.job_posting)
        
        improvements = []
        
        # Missing required skills
        if skill_match["missing_required"]:
            improvements.append(
                f"Learn these required skills to be a stronger candidate: "
                f"{', '.join(skill_match['missing_required'][:3])}"
            )
        
        # Missing preferred skills
        if skill_match["missing_preferred"]:
            improvements.append(
                f"Consider learning these preferred skills: "
                f"{', '.join(skill_match['missing_preferred'][:2])}"
            )
        
        # Experience gap
        if self.matcher.user_profile.years_experience < self.job_posting.experience_years:
            gap = self.job_posting.experience_years - self.matcher.user_profile.years_experience
            improvements.append(
                f"You're {gap} years short of the experience requirement. "
                f"Highlight quick wins and learning ability in your cover letter."
            )
        
        return improvements
    
    def generate_talking_points(self) -> List[str]:
        """Generate talking points for cover letter and interviews"""
        talking_points = []
        
        # Highlight matched skills
        skill_match = self.matcher.match_skills(self.job_posting)
        if skill_match["matched_required"]:
            talking_points.append(
                f"In your cover letter, emphasize your expertise in: "
                f"{', '.join(skill_match['matched_required'][:2])}"
            )
        
        # Role relevance
        current_role = self.matcher.user_profile.current_role
        job_title = self.job_posting.title
        talking_points.append(
            f"Frame your current {current_role} experience to show relevance to {job_title}"
        )
        
        # Company research suggestion
        talking_points.append(
            f"Research {self.job_posting.company}'s recent projects - mention in interview how you can contribute"
        )
        
        return talking_points
    
    def generate_interview_prep(self) -> Dict[str, List[str]]:
        """Generate potential interview questions and preparation tips"""
        skill_match = self.matcher.match_skills(self.job_posting)
        
        weak_areas = skill_match["missing_required"] + skill_match["missing_preferred"]
        
        prep = {
            "likely_questions": [
                f"Tell us about your experience with {skill_match['matched_required'][0] if skill_match['matched_required'] else 'this stack'}",
                f"Describe a challenging project in {self.matcher.user_profile.current_role}",
                f"Why are you interested in joining {self.job_posting.company}?"
            ],
            "preparation_tips": [
                f"Prepare examples using STAR method for {', '.join(skill_match['matched_required'][:2])}",
                "Prepare 2-3 questions about the role and team",
                f"Research {self.job_posting.company}'s recent news/product launches"
            ] if not weak_areas else [
                f"Be honest about learning {weak_areas[0]} - show willingness to learn",
                "Prepare examples using STAR method for your strongest matched skills",
                "Prepare 2-3 questions about the role and team"
            ]
        }
        
        return prep


class LinkedInAgent:
    """Main LinkedIn Job Application Assistant Agent"""
    
    def __init__(self, user_profile: UserProfile):
        self.user_profile = user_profile
    
    def analyze_job_posting(self, job_posting: JobPosting) -> Dict[str, any]:
        """Analyze a job posting and generate comprehensive application strategy"""
        
        matcher = JobMatcher(self.user_profile)
        advisor = ApplicationAdvisor(matcher, job_posting)
        
        match_score = matcher.calculate_match_score(job_posting)
        
        analysis = {
            "job_title": job_posting.title,
            "company": job_posting.company,
            "match_score": {
                "percentage": round(match_score, 1),
                "rating": self._rate_match(match_score)
            },
            "skill_analysis": matcher.match_skills(job_posting),
            "strong_points": advisor.generate_strong_points(),
            "improvement_areas": advisor.generate_improvement_areas(),
            "cover_letter_tips": advisor.generate_talking_points(),
            "interview_preparation": advisor.generate_interview_prep(),
            "recommendation": self._generate_recommendation(match_score)
        }
        
        return analysis
    
    def _rate_match(self, score: float) -> str:
        """Convert score to rating"""
        if score >= 80:
            return "Excellent Fit"
        elif score >= 60:
            return "Good Fit"
        elif score >= 40:
            return "Possible Fit"
        else:
            return "Challenging Fit"
    
    def _generate_recommendation(self, score: float) -> str:
        """Generate recommendation based on match score"""
        if score >= 80:
            return "Strong candidate - Apply with confidence! Emphasize matched skills."
        elif score >= 60:
            return "Good candidate - Apply. Work on highlighted missing skills."
        elif score >= 40:
            return "Consider applying - Close some skill gaps first if possible."
        else:
            return "Challenging fit - Consider gaining more skills before applying."


# Example usage
if __name__ == "__main__":
    # Create a sample user profile
    user_profile = UserProfile(
        name="John Smith",
        current_role="Senior Software Engineer",
        years_experience=6,
        skills=[
            "Python", "JavaScript", "React", "Node.js", "SQL", 
            "Docker", "AWS", "Git", "REST APIs", "Problem Solving"
        ],
        previous_roles=[
            "Software Engineer",
            "Junior Developer",
            "Intern"
        ],
        education="BS Computer Science",
        certifications=["AWS Solutions Architect"]
    )
    
    # Create a sample job posting
    job_posting = JobPosting(
        title="Senior Full Stack Engineer",
        company="TechCorp Inc",
        description="Looking for experienced full stack engineer...",
        required_skills=["Python", "React", "Node.js", "SQL", "Docker"],
        preferred_skills=["AWS", "Kubernetes", "TypeScript"],
        experience_years=5,
        seniority_level="Senior"
    )
    
    # Initialize agent and analyze
    agent = LinkedInAgent(user_profile)
    analysis = agent.analyze_job_posting(job_posting)
    
    # Display results
    print(json.dumps(analysis, indent=2))
