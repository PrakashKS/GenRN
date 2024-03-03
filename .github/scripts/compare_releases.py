import requests
import json

# Fetch the releases and commits from the GitHub API
repo_owner = "PrakashKS"
repo_name = "GenRN"
headers = {
    "Authorization": "Bearer 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",
    "Accept": "application/vnd.github.v3+json"
}

url_releases = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
url_commits = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"


response_releases = requests.get(url_releases, headers=headers)
releases_data = response_releases.json()

if 'message' in releases_data:
    error_message = releases_data['message']
    print(f"Error message: {error_message}")
    print(f"Documentation URL: {releases_data.get('documentation_url', 'N/A')}")
else:
    if releases_data:
        releases = releases_data
        if len(releases) >= 2:
            current_release = releases[0]
            previous_release = releases[1]
            
            print("Current Release:", current_release["name"])
            print("Previous Release:", previous_release["name"])
            

            
            
            response_current_commits = requests.get(f"{url_commits}?sha={current_release['tag_name']}", headers=headers)
            current_commits = response_current_commits.json()

            response_previous_commits = requests.get(f"{url_commits}?sha={previous_release['tag_name']}", headers=headers)
            previous_commits = response_previous_commits.json()

            # Compare commits and list detailed changelog
            for commit in current_commits:
            
                commit_sha = commit["sha"]
                tree_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/{commit_sha}"
                response_tree_url = requests.get(tree_url, headers=headers)
                response_data_tree_url = response_tree_url.json()
                
                print(response_data_tree_url);
                
                
                commit_message = commit["commit"]["message"]
                commit_author = commit["commit"]["author"]["name"]
                commit_date = commit["commit"]["author"]["date"]
                # print(commit)
                
                print("\n")  # Add a new line for better readability
                print("Commit Message:", commit_message)
                print("Commit Author:", commit_author)
                print("Commit Date:", commit_date)
                
                
                changed_files = []
                for file_tree in response_data_tree_url["tree"]:
                    if file_tree["type"] == "blob":  # Check for files (not directories)
                        changed_files.append(file_tree["path"])
                        print(file_tree["path"])

                     # Check if files key exists in the commit
                if "tree" in response_data_tree_url:
                    files_changed = [tree["path"] for tree in response_data_tree_url["tree"]]
                    if files_changed:
                        print("Changed Files:")
                        for file in files_changed:
                            print(file)
                    else:
                        print("No files changed in this commit")
                    # print(releases_data_to_get_files);
                else:
                    print("No files changed information available for this commit")
                
                
                
                print("\n")  # Add a new line for better readability
        else:
            print("Not enough releases to compare.")
    else:
        print("No releases found.")
        
        
        tree = response.json()
