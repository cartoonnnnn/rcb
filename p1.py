git --version
mkdir newproject
cd newproject
nano demo.py

# Write inside demo.py
print("Hello World")

git init
git config --global user.name "shreejitttt"
git config --global user.email "shreejitshah.cd23@bmsce.ac.in"

git status
git add demo.py
git commit -m "first commit"

nano demo.py

# Change code to
print("Hello Git")

git status
git diff
git add demo.py
git commit -m "main code added"

git branch add-feature
git checkout add-feature

nano demo.py

# Add feature code
print("Feature Added")

git status
git add demo.py
git commit -m "feature added"

git log
git checkout master
git merge add-feature

#Open GitHub
#Click New Repository
#Repository name:newproject
#Keep repository empty
#Click Create Repository

git remote add origin https://github.com/shreejitttt/newproject.git
git remote -v

# GitHub Token Steps
# Sign in GitHub
# Profile -> Settings
# Developer Settings -> Personal Access Tokens -> Tokens (Classic)
# Generate new token
# Add note
# Select No Expiration
# Check all boxes
# Generate token
# Copy and save token in text file

git push -u origin master

# Username = Your GitHub Username
# Password = paste Generated Token

# Verify repository on GitHub
#viva

1. What is Git?

Git is a distributed version control system used to track changes in files and manage source code efficiently.

2. Difference between Git and GitHub?
Git → local version control tool.
GitHub → online platform to host Git repositories.

3. What is the difference between git add and git commit?
git add → moves files to staging area.
git commit → permanently saves changes in repository history.

4. What is branching in Git?
Branching allows developers to work on new features separately without affecting the main code.

Example: git branch add-feature

5. What is the purpose of git push?
git push uploads local repository commits to a remote repository like GitHub.

Example:

git push -u origin master
