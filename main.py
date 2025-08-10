import json
import os

import pandas as pd
import requests
from dotenv import load_dotenv


def get_repo_details():
    try:
        load_dotenv()
        user = os.getenv("USER")
        pat = os.getenv("PAT")
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": pat
        }
        params = {
            "type": "owner",
            "sort": "full_name",
            "direction": "asc",
            "per_page": 30,
            "page": 1,
        }
        url = f"https://api.github.com/users/{user}/repos"
        res = requests.get(url, headers=headers, data=params, verify=True)
        df = pd.DataFrame(res.json())
        data = df.to_dict(orient="records")
        with open("repo_details.json", encoding="utf-8", mode="w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_repo_details()
