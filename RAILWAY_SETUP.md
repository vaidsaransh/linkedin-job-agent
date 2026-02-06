# Railway Deployment Guide

Deploy your LinkedIn Job Agent backend to Railway in 15 minutes!

## What is Railway?

Railway is a modern deployment platform that:
- ✅ Deploys Python apps easily
- ✅ Auto-deploys on git push
- ✅ Handles environment variables securely
- ✅ Costs ~$5-10/month
- ✅ Has free credits for new users

## Prerequisites

- ✅ GitHub repository with code pushed
- ✅ OpenAI API key (`sk-proj-...`)
- ✅ GitHub account (Railway uses it for login)
- ⏱️ 15 minutes of your time

## Step-by-Step Deployment

### Step 1: Create Railroad Account

1. Go to **[railway.app](https://railway.app)**
2. Click **"Start Project"** or **"Dashboard"**
3. Click **"New Project"**
4. Select **"Deploy from GitHub Repo"**
5. Authorize GitHub when prompted
6. Select your `linkedin-job-agent` repository

✅ **Done:** Railway will auto-detect Python and create the project

---

### Step 2: Configure Project

Railway should show:
```
Service: linkedin-job-agent
Type: Python
Port: 8000 (auto-detected)
```

If not, click the service and verify settings.

---

### Step 3: Add Environment Variables

#### From Railway Dashboard:

1. Click on your project
2. Click **"Variables"** tab
3. Click **"New Variable"** or **"RAW Editor"**

#### Add these variables:

**Using Form:**
```
OPENAI_API_KEY = sk-proj-YOUR_ACTUAL_KEY_HERE
FLASK_ENV = production
```

**Using Raw Editor:**
```
OPENAI_API_KEY=sk-proj-YOUR_ACTUAL_KEY_HERE
FLASK_ENV=production
```

⚠️ **IMPORTANT:** Never commit your actual API key to GitHub!
- Use `OPENAI_API_KEY` as the variable name
- Value = your actual API key starting with `sk-proj-`
- Railway keeps it secret

---

### Step 4: Deploy

1. Click **"Deploy"** button
2. Watch the build logs scroll by
3. Wait for "Build successful" message
4. Your app URL appears: `linkedin-job-agent-production.up.railway.app`

⏱️ **Takes:** 2-5 minutes

✅ **Deployment complete!**

---

## What Just Happened

Behind the scenes, Railway:
1. Cloned your repository
2. Installed `python` and dependencies from `requirements.txt`
3. Started `app.py` with `python app.py`
4. Assigned a public URL
5. Set up auto-redeployment on git push

---

## Access Your Deployed App

### Web Interface

Your app is now live at:
```
https://linkedin-job-agent-production.up.railway.app
```

Replace `linkedin-job-agent` with your actual project name if different.

### Test It

```bash
# Test the API
curl https://YOUR_URL/api/health

# Local test
export RAILWAY_URL="https://YOUR_URL"
python -c "import requests; print(requests.get('$RAILWAY_URL/api/health').json())"
```

---

## Update GitHub Pages

### Link from Landing Page

Edit `docs/index.html`:

**Find this:**
```html
<a href="demo.html" class="btn btn-primary">Launch Interactive Demo →</a>
```

**Replace with:**
```html
<div style="margin-top: 2rem;">
    <p>💻 <strong>Interactive Web Demo</strong> (no backend)</p>
    <a href="demo.html" class="btn btn-primary">Try JavaScript Demo</a>
    
    <p style="margin-top: 1rem;">🚀 <strong>Full App with AI</strong> (Python backend)</p>
    <a href="https://linkedin-job-agent-production.up.railway.app" class="btn btn-secondary">
        Launch Full App
    </a>
</div>
```

Then push to GitHub:
```bash
git add docs/index.html
git commit -m "Update links to Railway deployment"
git push origin main
```

---

## Redeploy When You Push Code

The best part: **No manual redeployment needed!**

### Automatic Redeployment

Every time you push to `main` branch:
```bash
git add .
git commit -m "New feature"
git push origin main
```

→ Railway automatically rebuilds and redeploys ✨

Monitor deployments in Railway dashboard → **Deployments** tab

---

## Verify Everything Works

### Test 1: Health Check
```bash
curl https://YOUR_URL/api/health
# Should return: {"status": "OK"}
```

### Test 2: Job Analysis
```bash
# In your local terminal:
python -c "
import requests
import json

url = 'https://YOUR_URL/api/analyze'
data = {
    'user_role': 'Frontend Developer',
    'user_skills': 'React, JavaScript, CSS',
    'job_title': 'React Developer',
    'job_skills': 'React, JavaScript, REST APIs'
}
response = requests.post(url, json=data)
print(json.dumps(response.json(), indent=2))
"
```

### Test 3: Web Interface
Just visit: `https://YOUR_URL` in your browser

---

## Environment Variables Reference

### Required
```
OPENAI_API_KEY = sk-proj-xxxxx
# Your OpenAI API key for AI features
```

### Optional
```
FLASK_ENV = production
# Set to 'production' for deployed app

PORT = 8000
# Usually auto-set, customize if needed

DEBUG = False
# Disable debug in production
```

---

## Troubleshooting

### Error: "Build failed"

**Check logs:**
1. Go to Railway dashboard
2. Click project → **"Logs"** tab
3. Scroll to find error message
4. Common causes:
   - Missing dependency in `requirements.txt`
   - Python syntax error
   - Missing file referenced in code

**Fix:**
```bash
# Fix locally
git add .
git commit -m "Fix deployment issue"
git push origin main
# Railway auto-rebuilds
```

### Error: "No module named 'flask'"

**Cause:** `requirements.txt` not updated

**Fix:**
```bash
# Locally, update requirements
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

### Slow Response Times

**First time:** ~5-10 seconds (container cold start)
**Subsequent:** ~100-200ms (normal)

**To improve:**
- Upgrade Railway plan ($7 → $15/month)
- Use caching (future feature)
- Optimize OpenAI calls

### OpenAI Quota Error

**Cause:** API key has no credits

**Fix:**
1. Go to [platform.openai.com/account/billing](https://platform.openai.com/account/billing)
2. Add payment method
3. Set usage limits ($5/month recommended)
4. Railway auto-retries with new key

---

## Cost Management

### Monitor Usage

**Railway Dashboard:**
1. Click project
2. **"Deployment"** tab
3. See RAM/CPU usage
4. Estimated bills

**OpenAI:**
1. https://platform.openai.com/account/usage
2. Track API calls
3. Set spending limit

### Reduce Costs

1. **Use gpt-4o-mini** (default) - ~$0.001 per analysis
2. **Set usage limits** in OpenAI dashboard
3. **Cache responses** (future feature)
4. **Batch requests** if possible

### Free Tier

**Railway:** $5/month free credits (new users)
**OpenAI:** $5 free trial (expires after 3 months)
**Total:** Can run for free initially!

---

## Advanced: Custom Domain

Want `myapp.com` instead of `railway.app` URL?

### Setup (10 minutes)

1. **Buy domain** - Namecheap, GoDaddy, etc.
2. **In Railway:**
   - Project → **Settings** → **Custom Domains**
   - Add your domain
   - Copy DNS records
3. **In domain provider:**
   - Update DNS with Railway's records
   - Wait 5-30 minutes for propagation

### Result
Your app now lives at: `https://myapp.com` ✨

---

## Advanced: Database Integration

Want to store application history?

Railway supports:
- ✅ PostgreSQL
- ✅ MongoDB
- ✅ MySQL
- ✅ Redis

### Simple Setup
1. Click **"Add Service"** in Railway
2. Choose database
3. Auto-generated connection string available
4. Update `app.py` to use it

---

## Monitoring & Logs

### View Real-Time Logs

```bash
# Install Railway CLI
npm install -g railway

# Login
railway login

# View logs
railway logs --follow
```

### GitHub Integration

Railway automatically:
- ✅ Reads from GitHub
- ✅ Checks for updates
- ✅ Rebuilds on push
- ✅ Deploys if valid

---

## What's Deployed

```
Your Railway App Structure:

linkedin-job-agent/
├── app.py (entrypoint)
├── linkedin_agent.py (core logic)
├── linkedin_utils.py (helpers)
├── llm_integration.py (AI features)
├── requirements.txt (dependencies)
└── ... (all other Python files)

Environment:
├── Python 3.10+
├── All pip packages from requirements.txt
├── Environment variables loaded
└── Port 8000 exposed publicly
```

---

## Next Steps

1. **Verify deployment works** (visit your URL)
2. **Test with real data** (try the web interface)
3. **Update GitHub Pages** (add link to Railway)
4. **Set up custom domain** (optional)
5. **Monitor usage** (stay within budget)

## Success! 🎉

You now have:
- ✅ Free GitHub Pages website
- ✅ Python backend on Railway
- ✅ OpenAI AI integration
- ✅ Auto-deployment on git push
- ✅ Real-world production setup

Total cost: **~$10/month** or less

Congratulations! Your project is live on the internet! 🚀

---

## Support

- **Railway Help:** https://docs.railway.app/
- **GitHub Issues:** Check your repo
- **OpenAI Docs:** https://platform.openai.com/docs/

Need help? Check Railway dashboard → **Help & Feedback** → **Support**
