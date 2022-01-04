import requests
import sys
import json


def get_github_commits(page: int):
    try:
        response = requests.get(
            url="https://api.github.com/repos/comme2e/comm/commits",
            params={
                "page": f"{page}",
                "per_page": "100",
            },
        )
    except requests.exceptions.RequestException:
        sys.exit("HTTP Request failed.")

    return response.json()


github_commit_data = []
for idx in range(50):
    github_commit_data.extend(get_github_commits(idx))

with open('github_commits.json', 'w') as github_fd:
    json.dump(github_commit_data, github_fd)
