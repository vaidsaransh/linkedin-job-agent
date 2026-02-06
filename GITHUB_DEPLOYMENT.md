# GitHub Deployment Guide - LinkedIn Job Application Assistant

This guide will help you deploy this project on GitHub and make it accessible online.

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `linkedin-job-agent` (or your preferred name)
3. Description: "AI-Powered LinkedIn Job Application Assistant"
4. Choose: Public
5. Click "Create repository"

## Step 2: Initialize Git & Push Code

From your project directory:

```bash
git init
git add .
git commit -m "Initial commit: LinkedIn Job Application Assistant with LLM integration"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/linkedin-job-agent.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 3: Setup GitHub Pages

1. Go to Settings → Pages (in your GitHub repo)
2. Source: Deploy from a branch
3. Branch: `main` / `/docs`
4. Click Save

## Step 4: Create Documentation Site

The docs folder will be served as your GitHub Pages website.

Files needed:
- docs/index.html (landing page)
- docs/README.md (documentation)
- docs/demo.html (interactive demo)
- docs/style.css (styling)

---

## Deployment Options

### Option A: GitHub Pages Only (Static Demo)
- ✅ Free, no additional setup
- ✅ Instant updates on push
- ❌ Python code runs in JavaScript, not real Python
- Use for: Showcase, documentation

### Option B: GitHub Pages + Deploy Service
- ✅ Real Python backend
- ✅ Full AI capabilities
- ✅ Free tier available
- Services: Railway, Render, Heroku (paid)

### Option C: GitHub Actions
- ✅ Run Python scripts
- ✅ Generate static content
- ✅ Automated workflows
- Use for: CI/CD, automated testing

---

## Recommended: Option B + GitHub Pages

### Deploy Flask Backend to Railway

1. Go to https://railway.app

2. Sign up with GitHub

3. Click "New Project" → "Deploy from GitHub Repo"

4. Select your linkedin-job-agent repo

5. Add environment variables:
   - OPENAI_API_KEY: your-api-key
   - FLASK_ENV: production

6. Deploy!

### Update GitHub Pages to Link to Deployed App

Edit docs/index.html to point to your Railway URL.

---

## .gitignore Setup

Make sure sensitive files aren't committed:

```
.env
.env.local
__pycache__/
*.pyc
.venv/
venv/
node_modules/
.DS_Store
*.egg-info/
dist/
build/
```

---

## GitHub Actions CI/CD Pipeline

Create `.github/workflows/deploy.yml` to:
- ✅ Run tests automatically
- ✅ Check code quality
- ✅ Deploy if tests pass

---

## Files Structure for GitHub Pages

```
your-repo/
├── docs/
│   ├── index.html          # Landing page
│   ├── demo.html           # Interactive demo
│   ├── style.css           # Styling
│   ├── script.js           # Frontend logic
│   └── README.md           # Documentation
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD pipeline
├── linkedin_agent.py
├── llm_integration.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## See Next Section for Generated Files
