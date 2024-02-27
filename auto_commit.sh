#!/bin/bash

# Navigate to your repository
cd /path/to/your/repo

# Make a trivial change to a file
echo " " >> keep_app_alive.txt

# Add the changed file to the staging area
git add keep_app_alive.txt

# Commit the change
git commit -m "Automated commit to keep Streamlit app alive"

# Push the commit to GitHub
git push origin main
