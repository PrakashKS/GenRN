import requests
import json

# Fetch the releases from the GitHub API
repo_owner = "PrakashKS"
repo_name = "GenRN"
headers = {
    "Authorization": "Bearer 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",
    "Accept": "application/vnd.github.v3+json"
}

url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
response = requests.get(url, headers=headers)
releases = response.json()

# Extract information about the current and previous releases
current_release = releases[0]  # Assuming the first release is the most recent
previous_release = releases[1] if len(releases) > 1 else None

# Compare the current release with the previous release
if previous_release:
    # Implement your comparison logic here
    # You can compare commit messages, pull requests, etc.
    # For simplicity, let's just print the names of the releases for demonstration
    print("Current Release:", current_release["name"])
    print("Previous Release:", previous_release["name"])
else:
    print("No previous release found.")

# Add logic to generate a diff or summary of changes between the releases
# This could involve comparing commit messages, pull requests, etc.
