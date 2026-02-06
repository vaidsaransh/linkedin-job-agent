"""
LLM Integration Module - adds real AI capabilities to LinkedIn Agent
Supports OpenAI and can be extended to other providers
"""

import os
from typing import Optional, List, Dict
from abc import ABC, abstractmethod


# Try to import OpenAI - if not installed, provide helpful error
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def generate_text(self, prompt: str, temperature: float = 0.7) -> str:
        """Generate text from prompt"""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if provider is available and configured"""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI LLM Provider"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o-mini"):
        """
        Initialize OpenAI provider
        
        Args:
            api_key: OpenAI API key (if None, uses OPENAI_API_KEY env var)
            model: Model to use (default: gpt-4o-mini for cost-effectiveness)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.client = None
        
        if self.api_key and OPENAI_AVAILABLE:
            self.client = OpenAI(api_key=self.api_key)
    
    def is_available(self) -> bool:
        """Check if OpenAI is available and configured"""
        return OPENAI_AVAILABLE and self.client is not None
    
    def generate_text(self, prompt: str, temperature: float = 0.7) -> str:
        """Generate text using OpenAI API"""
        if not self.is_available():
            raise RuntimeError(
                "OpenAI not available. Install with: pip install openai\n"
                "Then set OPENAI_API_KEY environment variable"
            )
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful career advisor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {e}")


class LLMEnhancedAnalyzer:
    """Enhances job analysis with LLM capabilities"""
    
    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize with LLM provider
        
        Args:
            llm_provider: LLM provider (default: None for rule-based only)
        """
        self.llm = llm_provider
        self.llm_available = llm_provider and llm_provider.is_available()
    
    def generate_personalized_cover_letter(
        self, 
        user_name: str,
        current_role: str,
        job_title: str,
        company: str,
        strong_points: List[str],
        skills: List[str]
    ) -> str:
        """
        Generate personalized cover letter opening using LLM
        
        Args:
            user_name: Candidate name
            current_role: Current job title
            job_title: Target job title
            company: Target company
            strong_points: Key strengths for this role
            skills: Key skills
        
        Returns:
            Generated cover letter opening paragraph
        """
        if not self.llm_available:
            return self._fallback_cover_letter(user_name, job_title, company)
        
        prompt = f"""
Write a compelling cover letter opening paragraph (2-3 sentences) for:
- Candidate: {user_name} ({current_role})
- Target Role: {job_title} at {company}
- Key Strengths: {', '.join(strong_points[:3])}
- Key Skills: {', '.join(skills[:5])}

Make it personalized, confident, and specific to the role. Focus on what they can contribute.
"""
        
        try:
            return self.llm.generate_text(prompt, temperature=0.7)
        except Exception as e:
            print(f"LLM error: {e}. Using fallback.")
            return self._fallback_cover_letter(user_name, job_title, company)
    
    def generate_interview_talking_points(
        self,
        user_background: str,
        job_requirements: str,
        matched_skills: List[str],
        missing_skills: List[str]
    ) -> List[str]:
        """
        Generate advanced interview talking points using LLM
        
        Args:
            user_background: Brief background
            job_requirements: Job description excerpt
            matched_skills: Skills candidate has
            missing_skills: Skills candidate lacks
        
        Returns:
            List of talking points for interview
        """
        if not self.llm_available:
            return self._fallback_talking_points(matched_skills)
        
        prompt = f"""
Generate 5 specific talking points for an interview for this job:

CANDIDATE BACKGROUND:
{user_background}

JOB REQUIREMENTS:
{job_requirements}

MATCHED SKILLS: {', '.join(matched_skills)}
MISSING SKILLS: {', '.join(missing_skills)}

Provide interview talking points that:
1. Highlight matched skills with specific examples
2. Address missing skills professionally (show willingness to learn)
3. Show understanding of job requirements
4. Are specific and memorable

Format as: point 1 | point 2 | point 3 | etc.
"""
        
        try:
            response = self.llm.generate_text(prompt, temperature=0.6)
            return [p.strip() for p in response.split('|')[:5]]
        except Exception as e:
            print(f"LLM error: {e}. Using fallback.")
            return self._fallback_talking_points(matched_skills)
    
    def analyze_job_fit_narrative(
        self,
        profile_summary: str,
        job_summary: str,
        match_percentage: float
    ) -> str:
        """
        Generate narrative analysis of job fit using LLM
        
        Args:
            profile_summary: Summary of candidate profile
            job_summary: Summary of job requirements
            match_percentage: Overall match percentage
        
        Returns:
            Narrative explanation of fit
        """
        if not self.llm_available:
            return self._fallback_fit_narrative(match_percentage)
        
        prompt = f"""
Provide a brief, insightful narrative (3-4 sentences) analyzing the job fit:

CANDIDATE:
{profile_summary}

JOB:
{job_summary}

MATCH SCORE: {match_percentage}%

Be honest but encouraging. Highlight key alignment points and growth opportunities.
"""
        
        try:
            return self.llm.generate_text(prompt, temperature=0.7)
        except Exception as e:
            print(f"LLM error: {e}. Using fallback.")
            return self._fallback_fit_narrative(match_percentage)
    
    def generate_learning_roadmap(
        self,
        missing_skills: List[str],
        priority_level: str = "high"
    ) -> Dict[str, List[str]]:
        """
        Generate learning roadmap for missing skills using LLM
        
        Args:
            missing_skills: List of skills to learn
            priority_level: "high" (ASAP), "medium", "low"
        
        Returns:
            Dictionary with learning steps and resources
        """
        if not self.llm_available:
            return self._fallback_learning_roadmap(missing_skills)
        
        prompt = f"""
Create a learning roadmap for someone who needs to learn these skills:
{', '.join(missing_skills)}

Priority: {priority_level}

For each skill, provide:
1. Why it matters
2. Learning resources (courses, tutorials, books)
3. Practice projects
4. Expected learning time

Format concisely for practical use.
"""
        
        try:
            response = self.llm.generate_text(prompt, temperature=0.5)
            return {
                "roadmap": response,
                "skills": missing_skills,
                "priority": priority_level
            }
        except Exception as e:
            print(f"LLM error: {e}. Using fallback.")
            return self._fallback_learning_roadmap(missing_skills)
    
    def generate_company_research_brief(
        self,
        company_name: str,
        industry: str
    ) -> str:
        """
        Generate company research talking points for interview
        
        Args:
            company_name: Name of company
            industry: Industry/sector
        
        Returns:
            Research talking points
        """
        if not self.llm_available:
            return f"Research {company_name}'s recent news and product launches"
        
        prompt = f"""
Based on general knowledge, provide 3-4 talking points about {company_name} ({industry}) that would be impressive in an interview:

Focus on:
- Recent company news/launches
- Industry position
- Culture indicators
- Growth areas

This should help demonstrate genuine interest in the company.
Be specific but use only well-known information.
"""
        
        try:
            return self.llm.generate_text(prompt, temperature=0.6)
        except Exception as e:
            print(f"LLM error: {e}. Using fallback.")
            return f"Research {company_name}'s recent news and product launches"
    
    def generate_salary_negotiation_tips(
        self,
        role: str,
        experience_years: int,
        location: str = "US"
    ) -> List[str]:
        """
        Generate salary negotiation tips
        
        Args:
            role: Job title
            experience_years: Years of experience
            location: Geographic location
        
        Returns:
            List of negotiation tips
        """
        if not self.llm_available:
            return self._fallback_salary_tips()
        
        prompt = f"""
Generate 5 practical salary negotiation tips for:
- Role: {role}
- Experience: {experience_years} years
- Location: {location}

Tips should address:
1. How to research fair market rate
2. When/how to bring up compensation
3. How to justify your ask
4. How to negotiate beyond salary
5. Red flags to watch for

Format as concise, actionable tips.
"""
        
        try:
            response = self.llm.generate_text(prompt, temperature=0.6)
            return [t.strip() for t in response.split('\n') if t.strip()][:5]
        except Exception as e:
            print(f"LLM error: {e}. Using fallback.")
            return self._fallback_salary_tips()
    
    # Fallback methods for rule-based alternatives
    
    @staticmethod
    def _fallback_cover_letter(name: str, job_title: str, company: str) -> str:
        """Rule-based fallback for cover letter"""
        return f"I am excited to apply for the {job_title} position at {company}. With my professional background and passion for this role, I am confident I can make a meaningful contribution to your team."
    
    @staticmethod
    def _fallback_talking_points(matched_skills: List[str]) -> List[str]:
        """Rule-based fallback for talking points"""
        return [
            f"Deep expertise in {', '.join(matched_skills[:2])}",
            "Proven track record delivering results",
            "Quick learner and problem solver",
            "Team player with strong communication",
            "Passionate about continuous improvement"
        ]
    
    @staticmethod
    def _fallback_fit_narrative(score: float) -> str:
        """Rule-based fallback for fit narrative"""
        if score >= 80:
            return "You're an excellent fit for this role. Your skills strongly align with the requirements, and you should apply with confidence."
        elif score >= 60:
            return "You're a good fit for this role with strong alignment on key skills. Consider addressing the noted skill gaps to be even more competitive."
        elif score >= 40:
            return "There's potential here, but you may want to develop some key skills first. The role is achievable with focused learning."
        else:
            return "This role requires different skill focus. Consider roles more aligned with your current profile, or invest time in learning the required skills."
    
    @staticmethod
    def _fallback_learning_roadmap(skills: List[str]) -> Dict[str, List[str]]:
        """Rule-based fallback for learning roadmap"""
        return {
            "roadmap": f"Focus on learning: {', '.join(skills)}. Break each skill into achievable milestones. Start with fundamentals, then practice with projects.",
            "skills": skills,
            "priority": "high"
        }
    
    @staticmethod
    def _fallback_salary_tips() -> List[str]:
        """Rule-based fallback for salary tips"""
        return [
            "Research market rates for your role on Glassdoor, Levels.fyi, and Payscale",
            "Wait until they ask about salary - let them anchor first",
            "Justify your ask with specific achievements and market data",
            "Negotiate other benefits: PTO, remote work, signing bonus, stock options",
            "Don't accept the first offer - professional negotiations are expected"
        ]


def get_llm_analyzer(use_openai: bool = True, api_key: Optional[str] = None) -> LLMEnhancedAnalyzer:
    """
    Factory function to create LLM analyzer
    
    Args:
        use_openai: Whether to try to use OpenAI
        api_key: OpenAI API key (optional, uses env var if not provided)
    
    Returns:
        LLMEnhancedAnalyzer (with or without LLM)
    """
    if use_openai and OPENAI_AVAILABLE:
        try:
            provider = OpenAIProvider(api_key=api_key)
            if provider.is_available():
                return LLMEnhancedAnalyzer(provider)
        except Exception as e:
            print(f"Warning: Could not initialize OpenAI: {e}")
    
    # Fall back to rule-based
    return LLMEnhancedAnalyzer(llm_provider=None)
