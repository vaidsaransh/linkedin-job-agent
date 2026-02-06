# GitHub Setup & Deployment Guide

## Quick Start (5 minutes)

### Step 1: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. **Repository name**: `linkedin-job-agent`
3. **Description**: "AI-Powered LinkedIn Job Application Assistant"
4. **Public** (so anyone can access)
5. Click **"Create repository"**

### Step 2: Clone to Your Local Machine (or Initialize)

If creating fresh:
```bash
cd ~/Desktop/Python
git init
git add .
git commit -m "Initial commit: LinkedIn Job Application Assistant"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/linkedin-job-agent.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (gear icon)
3. Left sidebar → **Pages**
4. **Source**: Select "Deploy from a branch"
5. **Branch**: Select `main`
6. **Folder**: Select `/ (root)` or `/docs` (both work, we use /docs)
7. Click **Save**

Wait 1-2 minutes, then your site will be live at: `https://YOUR_USERNAME.github.io/linkedin-job-agent/`

---

## File Structure Already Created

```
linkedin-job-agent/
├── docs/                          # ← GitHub Pages content
│   ├── index.html                # Landing page
│   ├── demo.html                 # Interactive demo
│   ├── style.css                 # Styling
│   └── README.md                 # Documentation
├── .github/
│   └── workflows/
│       └── deploy.yml            # CI/CD pipeline (automated)
├── .gitignore                    # What Git should ignore
├── linkedin_agent.py             # Core agent
├── linkedin_utils.py             # Utilities
├── llm_integration.py            # LLM features
├── app.py                        # Flask web app
├── requirements.txt              # Dependencies
├── test_suite.py                 # Tests
├── README.md                     # Documentation
└── [other Python files]
```

---

## What Each Component Does

### 📄 GitHub Pages (`/docs` folder)
- **landing page** (`index.html`) - Overview, features, CTA
- **demo page** (`demo.html`) - Interactive JavaScript demo (no backend needed!)
- **styling** (`style.css`) - Beautiful responsive design
- Publicly accessible at `https://YOUR_USERNAME.github.io/linkedin-job-agent/`

### ⚙️ GitHub Actions (`.github/workflows/deploy.yml`)
- **Automatically runs tests** when you push code
- **Tests on Python 3.10, 3.11, 3.12** for compatibility
- **Automatically deploys** `/docs` folder to GitHub Pages
- ✅ No manual deployment needed!

### 📦 Python Backend
- **Users can clone and run locally** with `python demo.py`
- **Run the Flask app** with `python app.py`
- **Full LLM integration** with OpenAI GPT

---

## Deployment Options

### Option 1: GitHub Pages Only (Recommended for Showcase)
✅ **What you get:**
- Free hosted website
- Interactive demo (JavaScript-based, no backend)
- Full documentation
- Updated automatically when you push

❌ **What you don't get:**
- Live Python code execution
- Real AI responses (unless you connect an API)

**Setup time:** 5 minutes ✨

### Option 2: GitHub Pages + Backend Service (Full Features)
✅ **What you get:**
- Everything in Option 1
- + Real Python backend running
- + Live AI responses from OpenAI
- + Full-featured REST API

❌ **What you don't get:**
- Completely free tier (small monthly cost)

**Free options:**
- Railway: Free tier (~$5/month useful)
- Render: Free tier (limited uptime)
- Heroku: Paid only now ($7+/month)

**Setup time:** 15-20 minutes

---

## Option 2 Deep Dive: Railway Deployment

### Step 1: Deploy Backend to Railway

1. Go to [railway.app](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub Repo"**
4. Authorize GitHub & select your `linkedin-job-agent` repo
5. Railway auto-detects Python + will show:
   - Service name: `linkedin-job-agent`
   - Root directory: `/` (correct)

### Step 2: Add Environment Variables

In Railway dashboard:
1. Go to **Variables** tab
2. Add:
   ```
   OPENAI_API_KEY = sk-proj-xxxxx
   FLASK_ENV = production
   PORT = 8000
   ```

### Step 3: Deploy

Click **"Deploy"** - Railway will:
- Install `requirements.txt`
- Start `app.py` automatically
- Give you a URL like `linkedin-job-agent-production.up.railway.app`

### Step 4: Update GitHub Pages

Edit `docs/index.html` to link to your Railway URL:
```html
<a href="https://linkedin-job-agent-production.up.railway.app" class="btn btn-primary">
  Launch Full App
</a>
```

---

## Making Changes & Pushing Updates

### Local Development:
```bash
# Make changes to your code
# Test locally
python demo.py
python test_suite.py

# Stage changes
git add .

# Commit
git commit -m "Add cool new feature"

# Push to GitHub
git push origin main
```

### What Happens Automatically:
✅ GitHub Actions runs tests
✅ Tests pass → ✨ GitHub Pages auto-updates
✅ If using Railway → Backend auto-updates

---

## Troubleshooting

### GitHub Pages not showing?
1. Check Settings → Pages
2. Ensure source is set to `main` branch, `/docs` folder
3. Wait 2-3 minutes for deployment
4. Refresh with `Ctrl+Shift+R` (hard refresh)

### Interactive demo not working?
- Demo is pure JavaScript/HTML
- Doesn't need backend to work
- Check browser console: F12 → Console tab
- Look for any red error messages

### Backend deployment failed?
- Check Railway dashboard → Logs
- Ensure `requirements.txt` is up to date
- Verify all Python files are pushed with `git push`

### OpenAI API errors?
- Check API key is correct in `OPENAI_API_KEY`
- Verify billing is set up on OpenAI account
- Check current quota at platform.openai.com

---

## GitHub Pages Features to Explore

### Custom Domain (Optional)
1. Go to **Settings → Pages**
2. **Custom domain**: Enter your domain
3. Add DNS records to your domain provider

### Custom 404 Page (Optional)
Create `docs/404.html` for custom 404 error page

### Branch Deployment
1. Create a staging environment with `develop` branch
2. Deploy `main` to production, `develop` to staging

---

## Sharing Your Project

### GitHub
```
https://github.com/YOUR_USERNAME/linkedin-job-agent
```

### Live Demo
```
https://YOUR_USERNAME.github.io/linkedin-job-agent/
```

### Backend API (if deployed)
```
https://linkedin-job-agent-production.up.railway.app
```

---

## Next Steps

1. **Immediate (< 5 min):**
   - Complete Step 3: Enable GitHub Pages
   - Check your demo at `https://YOUR_USERNAME.github.io/linkedin-job-agent/`

2. **Soon (< 15 min):**
   - Try the interactive demo
   - Share the link with friends

3. **Later (optional):**
   - Deploy backend to Railway for full features
   - Add custom domain
   - Set up CI/CD alerts

---

## Support & Resources

- [GitHub Pages Docs](https://pages.github.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Railway Docs](https://docs.railway.app/)
- [Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---

## Your Repository After Setup

```
YOUR_USERNAME/linkedin-job-agent
├── Live demo: https://YOUR_USERNAME.github.io/linkedin-job-agent/
├── Code repo: https://github.com/YOUR_USERNAME/linkedin-job-agent
├── Interactive demo works immediately ✨
├── Tests run automatically
├── Optional: Backend deployed to Railway
└── Everything stays in sync!
```

**You're all set! 🎉**
