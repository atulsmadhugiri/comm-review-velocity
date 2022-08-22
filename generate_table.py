import json
import pandas as pd
from dateutil import parser

gh_file = open('github_commits.json')
gh_data = json.load(gh_file)
gh_file.close()

phab_file = open('phabricator_diffs.json')
phab_data = json.load(phab_file)
phab_file.close()

diff_stamp = {}
for diff in phab_data['result']:
    diff_stamp[diff["id"]] = int(diff["dateCreated"])

land_stamp = {}
for each in gh_data:
    msg = each["commit"]["message"]
    timestamp = parser.parse(each["commit"]["committer"]["date"])
    if "Differential Revision: " in msg and "https://phab.comm.dev/D" in msg:
        diff_id = msg.split("Differential Revision: ")[1].split(
            "https://phab.comm.dev/D"
        )[1]
        land_stamp[diff_id] = int(timestamp.timestamp())
    elif "Differential Revision: " in msg and "https://phabricator.ashoat.com/D" in msg:
        diff_id = msg.split("Differential Revision: ")[1].split(
            "https://phabricator.ashoat.com/D"
        )[1]
        land_stamp[diff_id] = int(timestamp.timestamp())


diff_id_series = pd.Series(land_stamp.keys())
arcdiff_series = pd.Series([diff_stamp[idx] for idx in land_stamp.keys()])
arcland_series = pd.Series([land_stamp[idx] for idx in land_stamp.keys()])

df = pd.DataFrame({
    "id": diff_id_series,
    "arcdiff": arcdiff_series,
    "arcland": arcland_series
})
df.set_index('id', inplace=True)
df.to_csv('table.csv')
