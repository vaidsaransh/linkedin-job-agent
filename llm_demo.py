"""
Enhanced LinkedIn Agent with LLM Integration
Shows how to use LLM capabilities alongside the rule-based system
"""

from linkedin_agent import LinkedInAgent, UserProfile, JobPosting
from llm_integration import get_llm_analyzer, OPENAI_AVAILABLE
import json


class EnhancedLinkedInAgent(LinkedInAgent):
    """Extended LinkedInAgent with LLM capabilities"""
    
    def __init__(self, user_profile: UserProfile, use_llm: bool = True, api_key: str = None):
        """
        Initialize with optional LLM
        
        Args:
            user_profile: User's LinkedIn profile
            use_llm: Whether to enable LLM features
            api_key: Optional OpenAI API key
        """
        super().__init__(user_profile)
        self.use_llm = use_llm and OPENAI_AVAILABLE
        self.llm_analyzer = get_llm_analyzer(use_openai=use_llm, api_key=api_key)
        self.llm_available = self.llm_analyzer.llm_available
    
    def analyze_job_posting(self, job_posting: JobPosting, include_llm: bool = True):
        """
        Enhanced analysis with LLM features
        
        Args:
            job_posting: Job to analyze
            include_llm: Whether to add LLM features to analysis
        
        Returns:
            Extended analysis dictionary
        """
        # Get base analysis from parent class
        base_analysis = super().analyze_job_posting(job_posting)
        
        # Add LLM features if enabled and available
        if include_llm and self.llm_available:
            base_analysis = self._enhance_with_llm(base_analysis, job_posting)
        
        return base_analysis
    
    def _enhance_with_llm(self, base_analysis: dict, job_posting: JobPosting) -> dict:
        """Add LLM-generated content to base analysis"""
        
        # Generate personalized cover letter opening
        cover_letter = self.llm_analyzer.generate_personalized_cover_letter(
            user_name=self.user_profile.name,
            current_role=self.user_profile.current_role,
            job_title=job_posting.title,
            company=job_posting.company,
            strong_points=base_analysis['strong_points'],
            skills=self.user_profile.skills
        )
        
        # Generate advanced interview talking points
        interview_points = self.llm_analyzer.generate_interview_talking_points(
            user_background=f"{self.user_profile.current_role} with {self.user_profile.years_experience} years",
            job_requirements=job_posting.description,
            matched_skills=base_analysis['skill_analysis']['matched_required'],
            missing_skills=base_analysis['skill_analysis']['missing_required']
        )
        
        # Generate narrative analysis
        narrative = self.llm_analyzer.analyze_job_fit_narrative(
            profile_summary=f"{self.user_profile.current_role} with {self.user_profile.years_experience} years experience",
            job_summary=f"{job_posting.title} at {job_posting.company}",
            match_percentage=base_analysis['match_score']['percentage']
        )
        
        # Generate company research points
        company_research = self.llm_analyzer.generate_company_research_brief(
            company_name=job_posting.company,
            industry="Tech"  # Could be extracted from job_posting
        )
        
        # Add LLM features to analysis
        base_analysis['llm_enhanced'] = {
            'personalized_cover_letter': cover_letter,
            'ai_interview_points': interview_points,
            'fit_narrative': narrative,
            'company_research': company_research
        }
        
        return base_analysis
    
    def get_learning_roadmap(self, job_posting: JobPosting) -> dict:
        """
        Generate learning roadmap for missing skills using LLM
        
        Args:
            job_posting: Target job
        
        Returns:
            Learning roadmap
        """
        from linkedin_agent import JobMatcher
        
        matcher = JobMatcher(self.user_profile)
        skills = matcher.match_skills(job_posting)
        
        roadmap = self.llm_analyzer.generate_learning_roadmap(
            missing_skills=skills['missing_required'],
            priority_level='high'
        )
        
        return {
            'target_job': f"{job_posting.title} at {job_posting.company}",
            'missing_skills': skills['missing_required'],
            **roadmap
        }
    
    def get_salary_negotiation_tips(self, job_title: str = None) -> dict:
        """
        Get salary negotiation tips for the target role
        
        Args:
            job_title: Job title (default: user's current role)
        
        Returns:
            Salary negotiation tips
        """
        role = job_title or self.user_profile.current_role
        
        tips = self.llm_analyzer.generate_salary_negotiation_tips(
            role=role,
            experience_years=self.user_profile.years_experience,
            location="US"
        )
        
        return {
            'role': role,
            'experience_years': self.user_profile.years_experience,
            'tips': tips
        }


def demo_basic_llm_enhancement():
    """Demo: Basic LLM enhancement"""
    print("\n" + "="*70)
    print("DEMO 1: Basic LLM Enhancement")
    print("="*70)
    
    profile = UserProfile(
        name="Sarah Chen",
        current_role="Frontend Developer",
        years_experience=4,
        skills=["JavaScript", "React", "CSS", "HTML", "Git"],
        previous_roles=["Junior Developer", "Intern"],
        education="BS Computer Science",
        certifications=["Google Cloud Associate"]
    )
    
    job = JobPosting(
        title="Senior Frontend Engineer",
        company="TechCorp",
        description="Lead frontend development for scalable web apps",
        required_skills=["JavaScript", "React", "CSS", "TypeScript"],
        preferred_skills=["Next.js", "Testing", "DevOps"],
        experience_years=5,
        seniority_level="Senior"
    )
    
    print("\nInitializing Enhanced Agent...")
    agent = EnhancedLinkedInAgent(profile, use_llm=True)
    
    if agent.llm_available:
        print("✓ LLM is ENABLED - using AI to enhance analysis\n")
    else:
        print("⚠ LLM not available - using rule-based analysis\n")
        print("To enable LLM:")
        print("  1. pip install openai python-dotenv")
        print("  2. Set OPENAI_API_KEY environment variable")
        print("  3. Copy .env.example to .env and fill in your API key\n")
    
    print("Analyzing job posting...")
    analysis = agent.analyze_job_posting(job, include_llm=True)
    
    print(f"\nJob: {analysis['job_title']} at {analysis['company']}")
    print(f"Match Score: {analysis['match_score']['percentage']}%")
    print(f"Recommendation: {analysis['recommendation']}\n")
    
    if agent.llm_available and 'llm_enhanced' in analysis:
        llm = analysis['llm_enhanced']
        
        print("="*70)
        print("LLM-ENHANCED FEATURES")
        print("="*70)
        
        print("\n📝 PERSONALIZED COVER LETTER OPENING:")
        print(f"  {llm['personalized_cover_letter']}\n")
        
        print("💡 AI-GENERATED INTERVIEW TALKING POINTS:")
        for i, point in enumerate(llm['ai_interview_points'], 1):
            print(f"  {i}. {point}")
        
        print(f"\n📊 AI NARRATIVE ANALYSIS:")
        print(f"  {llm['fit_narrative']}\n")
        
        print("🏢 COMPANY RESEARCH POINTS:")
        print(f"  {llm['company_research']}\n")


def demo_learning_roadmap():
    """Demo: LLM-generated learning roadmap"""
    print("\n" + "="*70)
    print("DEMO 2: LLM Learning Roadmap")
    print("="*70)
    
    profile = UserProfile(
        name="Alex Johnson",
        current_role="Backend Developer",
        years_experience=3,
        skills=["Python", "SQL", "Docker"],
        previous_roles=["Junior Dev"],
        education="BS CS",
        certifications=[]
    )
    
    job = JobPosting(
        title="Senior DevOps Engineer",
        company="CloudCorp",
        description="Manage cloud infrastructure",
        required_skills=["Kubernetes", "AWS", "Terraform", "CI/CD"],
        preferred_skills=["Go", "Prometheus"],
        experience_years=5,
        seniority_level="Senior"
    )
    
    agent = EnhancedLinkedInAgent(profile, use_llm=True)
    
    if agent.llm_available:
        print("\n🤖 Generating AI-powered learning roadmap...\n")
        roadmap = agent.get_learning_roadmap(job)
        
        print(f"Target: {roadmap['target_job']}")
        print(f"Skills to Learn: {', '.join(roadmap['missing_skills'])}\n")
        print("LEARNING ROADMAP:")
        print(roadmap['roadmap'])
    else:
        print("LLM not available - run without LLM demo instead")


def demo_salary_negotiation():
    """Demo: Salary negotiation tips"""
    print("\n" + "="*70)
    print("DEMO 3: LLM Salary Negotiation Tips")
    print("="*70)
    
    profile = UserProfile(
        name="Jordan Smith",
        current_role="Senior Frontend Engineer",
        years_experience=6,
        skills=["React", "TypeScript", "Node.js"],
        previous_roles=["Frontend Dev", "Junior Dev"],
        education="BS CS",
        certifications=[]
    )
    
    agent = EnhancedLinkedInAgent(profile, use_llm=True)
    
    if agent.llm_available:
        print("\n💰 Generating salary negotiation tips...\n")
        tips = agent.get_salary_negotiation_tips("Senior Frontend Engineer")
        
        print(f"Role: {tips['role']}")
        print(f"Experience: {tips['experience_years']} years\n")
        print("NEGOTIATION TIPS:")
        for i, tip in enumerate(tips['tips'], 1):
            print(f"  {i}. {tip}\n")
    else:
        print("LLM not available - set up OpenAI integration to use this feature")


def demo_comparison_with_without_llm():
    """Demo: Compare analysis with and without LLM"""
    print("\n" + "="*70)
    print("DEMO 4: With and Without LLM Comparison")
    print("="*70)
    
    profile = UserProfile(
        name="Casey Davis",
        current_role="Software Engineer",
        years_experience=5,
        skills=["Python", "JavaScript", "AWS", "Docker"],
        previous_roles=["Junior Dev"],
        education="BS CS",
        certifications=[]
    )
    
    job = JobPosting(
        title="Full Stack Engineer",
        company="StartupXYZ",
        description="Build scalable web applications",
        required_skills=["Python", "JavaScript", "React", "AWS"],
        preferred_skills=["TypeScript", "Kubernetes"],
        experience_years=4,
        seniority_level="Senior"
    )
    
    print("\n🔍 Analyzing WITHOUT LLM (rule-based)...")
    agent_no_llm = EnhancedLinkedInAgent(profile, use_llm=False)
    analysis_no_llm = agent_no_llm.analyze_job_posting(job, include_llm=False)
    
    print(f"Match: {analysis_no_llm['match_score']['percentage']}%")
    print(f"Recommendation: {analysis_no_llm['recommendation']}")
    
    print("\n🤖 Analyzing WITH LLM (AI-enhanced)...")
    agent_with_llm = EnhancedLinkedInAgent(profile, use_llm=True)
    analysis_with_llm = agent_with_llm.analyze_job_posting(job, include_llm=True)
    
    print(f"Match: {analysis_with_llm['match_score']['percentage']}%")
    print(f"Recommendation: {analysis_with_llm['recommendation']}")
    
    if agent_with_llm.llm_available and 'llm_enhanced' in analysis_with_llm:
        print("\n✨ EXTRA LLM FEATURES:")
        print("  ✓ Personalized cover letter")
        print("  ✓ AI interview talking points")
        print("  ✓ AI fit narrative")
        print("  ✓ Company research points")
    else:
        print("\n⚠ LLM not available - only rule-based features shown")


if __name__ == "__main__":
    print("\n" + "🤖 " + "="*66 + " 🤖")
    print("  LINKEDIN AGENT - LLM INTEGRATION DEMOS")
    print("🤖 " + "="*66 + " 🤖")
    
    # Show setup instructions
    if not OPENAI_AVAILABLE:
        print("\n⚠️  OpenAI library not installed")
        print("\nTo enable LLM features:")
        print("  1. pip install openai python-dotenv")
        print("  2. Get API key from https://platform.openai.com/api-keys")
        print("  3. cp .env.example .env")
        print("  4. Edit .env and add your OPENAI_API_KEY")
        print("\nRunning demos in rule-based mode (no LLM)...\n")
    else:
        print("\n✓ OpenAI library available")
        print("  Run: export OPENAI_API_KEY='your_key' then run this script")
        print("  Or: copy .env.example to .env and fill in your key\n")
    
    # Run demos
    demo_basic_llm_enhancement()
    demo_comparison_with_without_llm()
    
    # Only run LLM-specific demos if available
    if OPENAI_AVAILABLE:
        try:
            demo_learning_roadmap()
            demo_salary_negotiation()
        except Exception as e:
            print(f"\n⚠️  LLM demos skipped: {e}")
            print("Make sure OPENAI_API_KEY is set")
    else:
        print("\n" + "="*70)
        print("Install OpenAI to see LLM-powered learning roadmap and salary tips:")
        print("  pip install openai python-dotenv")
        print("="*70)
