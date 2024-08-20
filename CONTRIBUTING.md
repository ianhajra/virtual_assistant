# Contributing to Virtual Assistant

Thank you for considering contributing to our project! We welcome your ideas and code contributions. Here's how you can get involved:

## 1. Have an Idea? Make an Issue
If you have a suggestion, feature request, or find a bug, please create an issue first. This helps us keep track of potential improvements and issues.

## 2. Writing Code? Follow These Steps

### 2.1. Create a New Branch
When you're ready to start coding, please create a new branch from `develop`:

```bash
# Make sure you're on the develop branch
git checkout develop

# Pull the latest changes
git pull origin develop

# Create a new branch with a descriptive name
git checkout -b IssueNumber-Brief-Description
```

### 2.2. Add, Commit, and Push Changes
Once you've made changes to your code, follow these steps to add, commit, and push them:

```bash
# Stage all changes
git add -A

# Commit the changes with a descriptive message
git commit -m "#IssueNumber: Info About It"

# Push the changes to the remote branch and set the upstream branch
git push --set-upstream origin IssueNumber-Brief-Description
```

### 2.3. Open a Pull Request
Once your work is ready, push your branch to GitHub and open a pull request (PR) against the develop branch.