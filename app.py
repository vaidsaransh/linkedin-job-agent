"""
Flask Web Interface for LinkedIn Job Application Assistant
Provides a user-friendly web dashboard
"""

from flask import Flask, render_template, request, jsonify
import json
from linkedin_agent import LinkedInAgent, UserProfile, JobPosting
from linkedin_utils import ProfileValidator, InterviewSimulator

app = Flask(__name__)

# Store user profiles in memory (in production, use a database)
user_profiles = {}


@app.route('/')
def index():
    """Home page"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>LinkedIn Job Application Assistant</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 1000px;
                margin: 0 auto;
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                color: #0073b1;
                text-align: center;
            }
            .nav-buttons {
                display: flex;
                gap: 10px;
                justify-content: center;
                margin: 20px 0;
            }
            button {
                padding: 10px 20px;
                background-color: #0073b1;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #005a87;
            }
            .section {
                margin: 20px 0;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            input, textarea, select {
                width: 100%;
                padding: 8px;
                margin: 5px 0;
                border: 1px solid #ddd;
                border-radius: 4px;
                box-sizing: border-box;
            }
            .results {
                background-color: #f9f9f9;
                padding: 15px;
                border-left: 4px solid #0073b1;
                margin: 10px 0;
            }
            .score {
                font-size: 24px;
                font-weight: bold;
                color: #0073b1;
            }
            .match-rating-excellent { color: #28a745; }
            .match-rating-good { color: #ffc107; }
            .match-rating-possible { color: #fd7e14; }
            .match-rating-challenging { color: #dc3545; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>💼 LinkedIn Job Application Assistant</h1>
            <p style="text-align: center; color: #666;">
                Analyze job postings and get personalized application strategies
            </p>
            
            <div class="nav-buttons">
                <button onclick="showSection('analyze')">Analyze Job</button>
                <button onclick="showSection('create-profile')">Create Profile</button>
                <button onclick="showSection('interview')">Interview Prep</button>
            </div>
            
            <!-- Create Profile Section -->
            <div id="create-profile" class="section" style="display:none;">
                <h2>Create Your Profile</h2>
                <form id="profileForm">
                    <input type="text" id="name" placeholder="Full Name" required>
                    <input type="text" id="current_role" placeholder="Current Role" required>
                    <input type="number" id="years_experience" placeholder="Years of Experience" required>
                    <textarea id="skills" placeholder="Skills (comma separated)" rows="3" required></textarea>
                    <textarea id="previous_roles" placeholder="Previous Roles (comma separated)" rows="3"></textarea>
                    <input type="text" id="education" placeholder="Education" required>
                    <textarea id="certifications" placeholder="Certifications (comma separated)" rows="2"></textarea>
                    <button type="button" onclick="saveProfile()">Save Profile</button>
                </form>
                <div id="profile-status" style="color: green; margin-top: 10px;"></div>
            </div>
            
            <!-- Analyze Job Section -->
            <div id="analyze" class="section">
                <h2>Analyze Job Posting</h2>
                <form id="jobForm">
                    <input type="text" id="job_title" placeholder="Job Title" required>
                    <input type="text" id="company" placeholder="Company Name" required>
                    <textarea id="job_description" placeholder="Job Description" rows="5" required></textarea>
                    <textarea id="required_skills" placeholder="Required Skills (comma separated)" rows="2" required></textarea>
                    <textarea id="preferred_skills" placeholder="Preferred Skills (comma separated)" rows="2"></textarea>
                    <input type="number" id="experience_years" placeholder="Years Experience Required" required>
                    <select id="seniority_level">
                        <option value="Entry">Entry Level</option>
                        <option value="Mid">Mid Level</option>
                        <option value="Senior">Senior</option>
                        <option value="Lead">Lead</option>
                    </select>
                    <button type="button" onclick="analyzeJob()">Analyze This Job</button>
                </form>
                <div id="analysis-results"></div>
            </div>
            
            <!-- Interview Prep Section -->
            <div id="interview" class="section" style="display:none;">
                <h2>Interview Preparation</h2>
                <textarea id="prep_skills" placeholder="Skills for which to generate questions (comma separated)" rows="3"></textarea>
                <button onclick="generateInterviewQuestions()">Generate Questions</button>
                <div id="interview-results" style="margin-top: 20px;"></div>
            </div>
        </div>
        
        <script>
            let currentProfile = null;
            
            function showSection(sectionId) {
                document.querySelectorAll('.section').forEach(s => s.style.display = 'none');
                document.getElementById(sectionId).style.display = 'block';
            }
            
            function saveProfile() {
                const profile = {
                    name: document.getElementById('name').value,
                    current_role: document.getElementById('current_role').value,
                    years_experience: parseInt(document.getElementById('years_experience').value),
                    skills: document.getElementById('skills').value.split(',').map(s => s.trim()),
                    previous_roles: document.getElementById('previous_roles').value.split(',').map(s => s.trim()).filter(s => s),
                    education: document.getElementById('education').value,
                    certifications: document.getElementById('certifications').value.split(',').map(s => s.trim()).filter(s => s)
                };
                
                currentProfile = profile;
                document.getElementById('profile-status').innerHTML = '✓ Profile saved: ' + profile.name;
            }
            
            function analyzeJob() {
                if (!currentProfile) {
                    alert('Please create a profile first!');
                    showSection('create-profile');
                    return;
                }
                
                const job = {
                    title: document.getElementById('job_title').value,
                    company: document.getElementById('company').value,
                    description: document.getElementById('job_description').value,
                    required_skills: document.getElementById('required_skills').value.split(',').map(s => s.trim()),
                    preferred_skills: document.getElementById('preferred_skills').value.split(',').map(s => s.trim()),
                    experience_years: parseInt(document.getElementById('experience_years').value),
                    seniority_level: document.getElementById('seniority_level').value
                };
                
                fetch('/api/analyze', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({profile: currentProfile, job: job})
                })
                .then(r => r.json())
                .then(data => displayAnalysis(data));
            }
            
            function displayAnalysis(data) {
                let html = '<div class="results">';
                html += '<div class="score">' + data.match_score.percentage + '%</div>';
                html += '<div style="font-size: 16px; color: #0073b1;">' + data.match_score.rating + '</div>';
                html += '<p><strong>Recommendation:</strong> ' + data.recommendation + '</p>';
                
                html += '<h3>Strong Points</h3><ul>';
                data.strong_points.forEach(p => html += '<li>' + p + '</li>');
                html += '</ul>';
                
                html += '<h3>Areas to Improve</h3><ul>';
                data.improvement_areas.forEach(a => html += '<li>' + a + '</li>');
                html += '</ul>';
                
                html += '<h3>Cover Letter Tips</h3><ul>';
                data.cover_letter_tips.forEach(t => html += '<li>' + t + '</li>');
                html += '</ul>';
                
                html += '</div>';
                document.getElementById('analysis-results').innerHTML = html;
            }
            
            function generateInterviewQuestions() {
                const skills = document.getElementById('prep_skills').value.split(',').map(s => s.trim());
                
                fetch('/api/interview', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({skills: skills})
                })
                .then(r => r.json())
                .then(data => {
                    let html = '<h3>Technical Questions</h3><ol>';
                    data.technical.forEach(q => html += '<li>' + q + '</li>');
                    html += '</ol>';
                    
                    html += '<h3>Behavioral Questions</h3><ol>';
                    data.behavioral.forEach(q => html += '<li>' + q + '</li>');
                    html += '</ol>';
                    
                    document.getElementById('interview-results').innerHTML = html;
                });
            }
        </script>
    </body>
    </html>
    '''


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """API endpoint for job analysis"""
    data = request.json
    
    # Create profile object
    profile = UserProfile(
        name=data['profile']['name'],
        current_role=data['profile']['current_role'],
        years_experience=data['profile']['years_experience'],
        skills=data['profile']['skills'],
        previous_roles=data['profile']['previous_roles'],
        education=data['profile']['education'],
        certifications=data['profile']['certifications']
    )
    
    # Create job object
    job = JobPosting(
        title=data['job']['title'],
        company=data['job']['company'],
        description=data['job']['description'],
        required_skills=data['job']['required_skills'],
        preferred_skills=data['job']['preferred_skills'],
        experience_years=data['job']['experience_years'],
        seniority_level=data['job']['seniority_level']
    )
    
    # Analyze
    agent = LinkedInAgent(profile)
    analysis = agent.analyze_job_posting(job)
    
    return jsonify(analysis)


@app.route('/api/interview', methods=['POST'])
def api_interview():
    """API endpoint for interview preparation"""
    data = request.json
    skills = data['skills']
    
    return jsonify({
        'technical': InterviewSimulator.generate_technical_questions(skills),
        'behavioral': InterviewSimulator.generate_behavioral_questions()
    })


if __name__ == '__main__':
    print("Starting LinkedIn Job Application Assistant Web Interface...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
