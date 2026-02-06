"""
Utility functions for LinkedIn Agent
"""

import re
from typing import List, Dict
from linkedin_agent import JobPosting, UserProfile


class JobPostingParser:
    """Parse job postings from various formats"""
    
    @staticmethod
    def parse_from_text(text: str) -> Dict[str, any]:
        """Extract skill keywords from job description text"""
        
        # Common technical skills
        tech_skills = {
            "Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "PHP",
            "React", "Vue", "Angular", "Django", "Flask", "Spring", "FastAPI",
            "SQL", "MongoDB", "PostgreSQL", "MySQL", "Redis", "Elasticsearch",
            "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Terraform",
            "Git", "CI/CD", "Jenkins", "GitHub Actions", "REST APIs", "GraphQL",
            "Microservices", "ML", "AI", "TensorFlow", "PyTorch"
        }
        
        found_skills = set()
        for skill in tech_skills:
            if skill.lower() in text.lower():
                found_skills.add(skill)
        
        # Count years of experience
        years_match = re.search(r'(\d+)\+?\s*years?', text.lower())
        years = int(years_match.group(1)) if years_match else 3
        
        return {
            "skills": list(found_skills),
            "years": years
        }


class ProfileValidator:
    """Validate and score user profiles"""
    
    @staticmethod
    def calculate_profile_completeness(profile: UserProfile) -> float:
        """Return profile completeness score 0-100"""
        score = 0
        
        # Basic info (20 points)
        if profile.name:
            score += 5
        if profile.current_role:
            score += 5
        if profile.education:
            score += 5
        if profile.certifications:
            score += 5
        
        # Skills (30 points)
        if len(profile.skills) >= 5:
            score += 15
        elif len(profile.skills) >= 3:
            score += 10
        elif len(profile.skills) > 0:
            score += 5
        
        # Experience (30 points)
        if profile.years_experience >= 5:
            score += 15
        elif profile.years_experience >= 2:
            score += 10
        elif profile.years_experience > 0:
            score += 5
        
        if len(profile.previous_roles) >= 3:
            score += 15
        elif len(profile.previous_roles) >= 2:
            score += 10
        elif len(profile.previous_roles) > 0:
            score += 5
        
        # Certifications (20 points)
        if len(profile.certifications) >= 2:
            score += 20
        elif len(profile.certifications) >= 1:
            score += 10
        
        return min(100, score)
    
    @staticmethod
    def get_profile_improvement_suggestions(profile: UserProfile) -> List[str]:
        """Suggest profile improvements"""
        suggestions = []
        
        if len(profile.skills) < 5:
            suggestions.append("Add more skills to your profile (aim for at least 5)")
        
        if len(profile.certifications) == 0:
            suggestions.append("Consider adding relevant certifications to strengthen your profile")
        
        if not profile.education:
            suggestions.append("Add or update your education information")
        
        if len(profile.previous_roles) < 2:
            suggestions.append("Highlight more previous roles in your profile")
        
        return suggestions


class ApplicationTracker:
    """Track application history and success rates"""
    
    def __init__(self):
        self.applications = []
    
    def log_application(self, job_posting: JobPosting, match_score: float, applied: bool):
        """Log a job application"""
        self.applications.append({
            "job_title": job_posting.title,
            "company": job_posting.company,
            "match_score": match_score,
            "applied": applied,
            "timestamp": None  # Would be datetime in real implementation
        })
    
    def get_success_pattern(self) -> Dict[str, any]:
        """Analyze patterns in successful applications"""
        if not self.applications:
            return {"message": "No applications logged yet"}
        
        applied = [a for a in self.applications if a["applied"]]
        applied_scores = [a["match_score"] for a in applied]
        
        return {
            "total_applications": len(self.applications),
            "applied_count": len(applied),
            "average_match_score_applied": round(sum(applied_scores) / len(applied_scores), 1) if applied_scores else 0,
            "average_match_score_all": round(sum(a["match_score"] for a in self.applications) / len(self.applications), 1)
        }


class InterviewSimulator:
    """Generate mock interview scenarios"""
    
    @staticmethod
    def generate_technical_questions(skills: List[str]) -> List[str]:
        """Generate technical questions based on skills"""
        skill_questions = {
            "Python": "Explain the difference between lists and tuples in Python",
            "JavaScript": "What are closures in JavaScript and why are they important?",
            "React": "What is the purpose of useEffect in React hooks?",
            "SQL": "Explain the difference between JOIN and UNION in SQL",
            "Docker": "What are the advantages of using Docker containers?",
            "AWS": "What is the difference between EC2 and Lambda?",
            "Design Patterns": "Explain the Observer pattern and provide an example"
        }
        
        questions = []
        for skill in skills[:3]:
            if skill in skill_questions:
                questions.append(skill_questions[skill])
        
        if not questions:
            questions.append("Tell me about your most challenging project")
        
        return questions
    
    @staticmethod
    def generate_behavioral_questions() -> List[str]:
        """Generate behavioral interview questions"""
        return [
            "Tell me about a time you had to deal with a difficult team member",
            "Describe a situation where you had to learn a new technology quickly",
            "Give an example of when you had to adapt your approach to solve a problem",
            "Tell me about your greatest achievement in your career",
            "How do you handle failure or making mistakes at work?"
        ]
