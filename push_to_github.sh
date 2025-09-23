#!/bin/bash

# Push Jane Project to GitHub
# Usage: ./push_to_github.sh yourusername

if [ $# -eq 0 ]; then
    echo "❌ Please provide your GitHub username"
    echo "Usage: ./push_to_github.sh yourusername"
    echo "Example: ./push_to_github.sh johndoe"
    exit 1
fi

USERNAME=$1
REPO_NAME="jane-project"

echo "🚀 Setting up GitHub remote for $USERNAME/$REPO_NAME"

# Add remote origin
git remote add origin https://github.com/$USERNAME/$REPO_NAME.git

# Set main branch
git branch -M main

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully pushed to GitHub!"
    echo "🌐 Your repository is now available at:"
    echo "   https://github.com/$USERNAME/$REPO_NAME"
    echo ""
    echo "📝 Next steps:"
    echo "1. Visit your repository on GitHub"
    echo "2. Update the README.md with your repository URL"
    echo "3. Set up GitHub Pages if you want to host the documentation"
    echo "4. Configure GitHub Actions for CI/CD (optional)"
else
    echo "❌ Failed to push to GitHub"
    echo "💡 Make sure:"
    echo "1. You've created the repository on GitHub"
    echo "2. The repository name matches: $REPO_NAME"
    echo "3. You have write access to the repository"
    echo "4. Your Git credentials are configured"
fi
