# GitHub Contribution Graph Hacker 🚀

Automatically fill your GitHub contribution graph with backdated commits.

## ⚠️ Important Disclaimer

This tool is for **educational purposes and experimentation only**. Using fake commits to misrepresent your activity:
- May violate GitHub's Terms of Service
- Can damage your professional reputation if discovered
- Is easily detectable by experienced developers

**Better approach**: Use this repo to automate real mini-projects, daily coding exercises, or learning notes so your graph reflects genuine progress.

## 🎯 What This Does

The `generate_commits.py` script creates commits with backdated timestamps to fill in your GitHub contribution graph. It:
- Goes back 365 days from today
- Randomly selects days to commit (70% probability)
- Creates 1-5 commits per active day
- Uses `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables
- Appends to an `activity.log` file for each commit

## 📋 How to Use

### Step 1: Clone this repository locally

```bash
git clone https://github.com/MasteraSnackin/contribution-graph.git
cd contribution-graph
```

### Step 2: Configure git with your GitHub email

**CRITICAL**: The email must match your GitHub account email, or commits won't appear on your profile.

```bash
git config user.email "your-github-email@example.com"
git config user.name "Your Name"
```

### Step 3: Run the script

```bash
python3 generate_commits.py
```

This will generate hundreds of commits with dates spread throughout the past year.

### Step 4: Push to GitHub

```bash
git push origin main
```

### Step 5: Wait and refresh

GitHub may take a few minutes to reindex your contribution graph. Refresh your profile page to see the changes.

## ⚙️ Customization

Edit `generate_commits.py` to customize behavior:

```python
START_DATE = datetime.now() - timedelta(days=365)  # How far back
END_DATE = datetime.now()                          # End date
MIN_COMMITS_PER_DAY = 1                            # Min commits/day
MAX_COMMITS_PER_DAY = 5                            # Max commits/day
COMMIT_PROBABILITY = 0.7                           # % of days to commit
```

## 🔧 How It Works

GitHub counts a contribution if:
1. The commit is in the last 12 months
2. The commit email matches your GitHub account
3. It's on the default branch of a non-fork repo
4. The commit was made by you (not merged from someone else)

The script uses git's environment variables to backdate commits:
```python
env['GIT_AUTHOR_DATE'] = '2024-05-18 10:00:00'
env['GIT_COMMITTER_DATE'] = '2024-05-18 10:00:00'
```

## 🎨 Ethical Usage Ideas

Instead of fake commits, use this automation for real work:
- Daily LeetCode/coding challenge solutions
- Smart contract experiments (Solidity, Rust)
- Web3 research notes
- Blockchain development logs
- Learning journal entries

This way your graph is legitimately green AND you're building real skills.

## 📚 Related Resources

- [How GitHub counts contributions](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/why-are-my-contributions-not-showing-up-on-my-profile)
- [Git environment variables](https://git-scm.com/book/en/v2/Git-Internals-Environment-Variables)

## 📜 License

MIT - Use at your own risk. Not responsible for any consequences of using this tool.

---

**Remember**: A sparse but authentic contribution graph is infinitely more valuable than a fake green square wall. Use this wisely! 💚
