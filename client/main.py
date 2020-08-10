# IMPORTS
import requests
import json
from datetime import *
import os
from dotenv import load_dotenv

# Class
class githubClient:
    def __init__(
        self,
        api_url="https://api.github.com",
        labels=["Feature", "Opportunity", "Requirement", "bug", "enhancement"],
        org="snek-at",
        project_start=datetime(2020, 7, 15),
    ):
        # VARIABLES
        project_folder = os.path.expanduser("./")
        load_dotenv(os.path.join(project_folder, ".env"))
        self.api_url = api_url
        self.labels = ["Feature", "Opportunity", "Requirement", "bug", "enhancement"]
        self.org = org
        self.project_start = project_start

    # EXECUTION
    # Get all repository names from snek-at organization
    def getRepositories(self):
        repos = []

        with requests.get(
            f"{self.api_url}/users/{self.org}/repos?access_token={os.getenv('ACCESS_TOKEN')}"
        ) as repo_req:
            # Convert html response to json
            repo_json = json.loads(repo_req.text)

            for repo in repo_json:
                repos.append(repo["name"])

        # Return found repositories
        return repos
