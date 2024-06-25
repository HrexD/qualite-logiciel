import os
import openai
import json
from github import Github

# Récupérer les variables d'environnement
token = os.getenv('TOKEN')
repo_name = os.getenv('REPOSITORY')
pr_number = os.getenv('PR_NUMBER')

# Vérification si PR_NUMBER est fourni
if not pr_number:
    raise ValueError("PR_NUMBER n'est pas défini. Ce script doit être exécuté dans le contexte d'une pull request.")

# Initialiser l'instance Github
g = Github(token)
# Obtenir le dépôt spécifié
repo = g.get_repo(repo_name)
# Obtenir la pull request spécifiée
pull_request = repo.get_pull(int(pr_number))

# Récupérer les diffs des commits
diffs = []
for file in pull_request.get_files():
    diffs.append(file.patch)

# Utiliser GPT pour analyser les diffs
openai.api_key = os.getenv('OPENAI_API_KEY')
analysis_results = []

for diff in diffs:
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Analyze this code diff and provide a code review:\n{diff}",
        max_tokens=150
    )
    analysis_results.append(response.choices[0].text.strip())

# Enregistrer les résultats de l'analyse
with open('analysis_results.json', 'w') as f:
    json.dump(analysis_results, f)
