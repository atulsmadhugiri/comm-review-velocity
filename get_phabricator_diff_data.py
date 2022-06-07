import requests
import sys
import json
import os


def get_diff_data():
    try:
        response = requests.get(
            url="https://phab.comm.dev/api/differential.query",
            params={
                "api.token": os.getenv("PHABRICATOR_API_TOKEN")
            },
        )
    except requests.exceptions.RequestException:
        sys.exit("HTTP Request failed.")

    return response.json()


phabricator_diff_data = get_diff_data()
with open('phabricator_diffs.json', 'w') as phabricator_fd:
    json.dump(phabricator_diff_data, phabricator_fd)
