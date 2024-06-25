import os
import json
from github import Github

# Récupérer les variables d'environnement
token = os.getenv('TOKEN')
repo_name = os.getenv('REPOSITORY')
pr_number = os.getenv('PR_NUMBER')

g = Github(token)
repo = g.get_repo(repo_name)
pull_request = repo.get_pull(int(pr_number))

# Charger les résultats de l'analyse
with open('analysis_results.json') as f:
    analysis_results = json.load(f)

# Ajouter des commentaires à la pull request
for comment in analysis_results:
    pull_request.create_issue_comment(comment)
