"""
LLM Integration Setup Guide
Complete instructions for adding AI capabilities
"""


print("""
╔════════════════════════════════════════════════════════════════════════════╗
║           LLM INTEGRATION SETUP - LINKEDIN AGENT                            ║
╚════════════════════════════════════════════════════════════════════════════╝

🎯 WHAT LLM INTEGRATION ADDS:

✨ AI-Powered Features:
  ✓ Personalized cover letter generation
  ✓ AI interview talking points
  ✓ Narrative job fit analysis
  ✓ Company research brief
  ✓ Learning roadmap generation
  ✓ Salary negotiation tips
  
⚙️  How It Works:
  • Hybrid System: Rule-based + AI
  • Graceful Fallback: Works without OpenAI (uses templates)
  • Cost-Effective: Uses gpt-4o-mini (fastest, cheapest model)
  • Zero Breaking Changes: Fully backward compatible

════════════════════════════════════════════════════════════════════════════

📋 SETUP INSTRUCTIONS:

STEP 1: Install Dependencies
────────────────────────────────────────────────────────────────────────────
  pip install -r requirements.txt

This installs:
  • openai==1.3.0 (OpenAI Python client)
  • python-dotenv==1.0.0 (Environment variable management)


STEP 2: Get OpenAI API Key
────────────────────────────────────────────────────────────────────────────
  1. Go to: https://platform.openai.com/api-keys
  2. Sign up or log in (free account)
  3. Create a new API key
  4. Copy the key (you'll need it in next step)
  5. Note: You need paid credits to use the API (~$5 gets you far)


STEP 3: Configure Environment
────────────────────────────────────────────────────────────────────────────
  Option A - Using .env file (Recommended):
    1. cp .env.example .env
    2. Edit .env and add your API key:
       OPENAI_API_KEY=sk-your-key-here
       OPENAI_MODEL=gpt-4o-mini

  Option B - Using environment variable:
    export OPENAI_API_KEY="sk-your-key-here"


STEP 4: Test Installation
────────────────────────────────────────────────────────────────────────────
  python llm_demo.py
  
  You should see:
  ✓ "LLM is ENABLED"
  ✓ AI-generated cover letter opening
  ✓ AI interview talking points
  ✓ And more...


════════════════════════════════════════════════════════════════════════════

💻 HOW TO USE LLM FEATURES:

BASIC USAGE:
────────────────────────────────────────────────────────────────────────────
  from linkedin_agent import UserProfile, JobPosting
  from llm_integration import EnhancedLinkedInAgent
  
  # Create agent with LLM enabled (requires API key)
  agent = EnhancedLinkedInAgent(profile, use_llm=True)
  
  # Get analysis with AI features
  analysis = agent.analyze_job_posting(job, include_llm=True)
  
  # Access LLM features
  if 'llm_enhanced' in analysis:
      print(analysis['llm_enhanced']['personalized_cover_letter'])
      print(analysis['llm_enhanced']['ai_interview_points'])
      print(analysis['llm_enhanced']['fit_narrative'])
      print(analysis['llm_enhanced']['company_research'])


LEARNING ROADMAP:
────────────────────────────────────────────────────────────────────────────
  roadmap = agent.get_learning_roadmap(job)
  print(roadmap['roadmap'])  # AI-generated learning path


SALARY NEGOTIATION TIPS:
────────────────────────────────────────────────────────────────────────────
  tips = agent.get_salary_negotiation_tips("Senior Frontend Engineer")
  for tip in tips['tips']:
      print(f"- {tip}")


WITHOUT LLM (Falls Back to Templates):
────────────────────────────────────────────────────────────────────────────
  agent = EnhancedLinkedInAgent(profile, use_llm=False)
  # Still works! Uses rule-based fallbacks instead of AI


════════════════════════════════════════════════════════════════════════════

📊 LLM TOKEN USAGE & COSTS:

Model: gpt-4o-mini (recommended for cost)
────────────────────────────────────────────────────────────────────────────
  Input:  $0.15 per 1M tokens
  Output: $0.60 per 1M tokens
  
  Typical Job Analysis:
  • Tokens per analysis: ~1500 input + ~500 output
  • Cost per analysis: ~$0.0011 (fraction of a cent!)
  • Credit usage: $5 = ~4,500 job analyses


Model: gpt-4o (more powerful, higher cost)
────────────────────────────────────────────────────────────────────────────
  Input:  $5 per 1M tokens
  Output: $15 per 1M tokens
  
  Cost per analysis: ~$0.03 (slightly higher)
  $5 = ~165 job analyses


════════════════════════════════════════════════════════════════════════════

🔧 AVAILABLE LLM FEATURES:

1. Personalized Cover Letter
   ├─ Analyzes your skills + job requirements
   ├─ Generates custom opening paragraph
   └─ Better than generic templates

2. AI Interview Talking Points
   ├─ Specific to job requirements
   ├─ Addresses skill gaps professionally
   └─ Memorable and compelling

3. Job Fit Narrative
   ├─ Explains why you're well/poorly fit
   ├─ Not just a percentage
   └─ Actionable insights

4. Company Research Brief
   ├─ Talking points to impress in interview
   ├─ Shows genuine research
   └─ Current knowledge based

5. Learning Roadmap
   ├─ Step-by-step path to learn missing skills
   ├─ Resource recommendations
   ├─ Timeline estimates
   └─ Practice project ideas

6. Salary Negotiation Tips
   ├─ Market rate research strategy
   ├─ Negotiation tactics
   ├─ What to ask for beyond salary
   └─ Red flags to watch


════════════════════════════════════════════════════════════════════════════

🛡️  SECURITY & PRIVACY:

API Key Security:
  ✓ Never commit .env to git (it's in .gitignore by default)
  ✓ API key only sent to OpenAI
  ✓ Consider rotating key periodically
  ✓ Set usage limits in OpenAI dashboard

Data Privacy:
  • Input data goes to OpenAI servers
  • Job descriptions/profiles are processed by OpenAI
  • OpenAI retains data for 30 days for abuse detection
  ⚠️  Don't use with sensitive/confidential information


════════════════════════════════════════════════════════════════════════════

🚨 TROUBLESHOOTING:

ERROR: "OpenAI not available"
────────────────────────────────────────────────────────────────────────────
  Solution: pip install openai python-dotenv


ERROR: "API key not found"
────────────────────────────────────────────────────────────────────────────
  Check:
  1. .env file exists and has OPENAI_API_KEY=sk-...
  2. Or environment variable: echo $OPENAI_API_KEY
  3. Key format: should start with "sk-"


ERROR: "Authentication failed"
────────────────────────────────────────────────────────────────────────────
  • API key is wrong/expired
  • Get new key from https://platform.openai.com/api-keys
  • Update .env or environment variable


ERROR: "Rate limit exceeded"
────────────────────────────────────────────────────────────────────────────
  • Made too many requests
  • Wait 60 seconds before retrying
  • Consider upgrading your OpenAI usage tier


ERROR: "Insufficient credits"
────────────────────────────────────────────────────────────────────────────
  • Account ran out of credits
  • Add payment method at https://platform.openai.com/account/billing/overview
  • Add $5-20 to get started


════════════════════════════════════════════════════════════════════════════

✨ BEST PRACTICES:

1. Hybrid Approach
   • Use rule-based for speed (instant)
   • Use LLM when quality matters (personalization)

2. Caching Results
   • Cache LLM responses locally
   • Don't regenerate for same job
   • Saves tokens and cost

3. Error Handling
   • LLM failures don't break the app
   • Automatically falls back to templates
   • User sees rules-based output

4. Monitoring Costs
   • Check OpenAI dashboard regularly
   • Set usage alerts
   • Regular cleanup of old results


════════════════════════════════════════════════════════════════════════════

📚 EXAMPLE CODE:

EXAMPLE 1: Full Enhanced Analysis
────────────────────────────────────────────────────────────────────────────
from linkedin_agent import UserProfile, JobPosting
from llm_integration import EnhancedLinkedInAgent

profile = UserProfile(
    name="Jane Doe",
    current_role="Developer",
    years_experience=5,
    skills=["Python", "React", "AWS"],
    previous_roles=["Junior Dev"],
    education="BS CS",
    certifications=[]
)

job = JobPosting(
    title="Senior Developer",
    company="TechCorp",
    description="...",
    required_skills=["Python", "React"],
    preferred_skills=["AWS", "Docker"],
    experience_years=5,
    seniority_level="Senior"
)

# Create agent with LLM
agent = EnhancedLinkedInAgent(profile, use_llm=True)

# Get full analysis
analysis = agent.analyze_job_posting(job)

# Use results
print(f"Match: {analysis['match_score']['percentage']}%")
if 'llm_enhanced' in analysis:
    print("Cover Letter:", analysis['llm_enhanced']['personalized_cover_letter'])
    print("Interview Tips:", analysis['llm_enhanced']['ai_interview_points'])


EXAMPLE 2: Generate Learning Path
────────────────────────────────────────────────────────────────────────────
roadmap = agent.get_learning_roadmap(job)
print("Target Job:", roadmap['target_job'])
print("Skills to Learn:", roadmap['missing_skills'])
print("\\nRoadmap:")
print(roadmap['roadmap'])


EXAMPLE 3: Salary Tips
────────────────────────────────────────────────────────────────────────────
tips = agent.get_salary_negotiation_tips("Senior Developer")
for i, tip in enumerate(tips['tips'], 1):
    print(f"{i}. {tip}")


════════════════════════════════════════════════════════════════════════════

❓ FAQ:

Q: Do I need an OpenAI account?
A: Yes, but it's free to create. You do need to add payment method to use API.

Q: Can I use other LLM providers?
A: Architecture supports it! You can extend LLMProvider class for Claude, 
   Llama, etc.

Q: What if I don't have API key?
A: Agent still works! Falls back to rule-based templates automatically.

Q: How much will it cost?
A: ~$0.001 per analysis with gpt-4o-mini. $5 = 4,500+ analyses.

Q: Is my data private?
A: OpenAI sees job descriptions and profiles. Don't use confidential info.

Q: Can I cache results?
A: Yes! Extend EnhancedLinkedInAgent to add caching layer.

Q: Which model should I use?
A: gpt-4o-mini (default) - best balance of cost and quality


════════════════════════════════════════════════════════════════════════════

🎓 NEXT STEPS:

1. Install: pip install -r requirements.txt
2. Setup: Set OPENAI_API_KEY environment variable
3. Test: python llm_demo.py
4. Use: Integrate into your LinkedIn Agent
5. Extend: Add more LLM features as needed

════════════════════════════════════════════════════════════════════════════
""")
