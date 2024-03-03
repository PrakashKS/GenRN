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

print("Response Status Code:", response.status_code)
print("Response Content:")
print(response.content)

data = response.json()

#print("Printing the data element")
#print(data)

if 'message' in data:
    error_message = data['message']
    print(f"Error message: {error_message}")
    print(f"Documentation URL: {data.get('documentation_url', 'N/A')}")
else:
    # Check if the response contains any releases
    if data:
        releases = data
        if releases:
            current_release = releases[0]  # Assuming the first release is the most recent
            print("Current Release:", current_release["name"])
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
        else:
            print("No releases found.")
    else:
        print("Failed to retrieve release data from the API.")
        
#This is for the comparing the version 2
