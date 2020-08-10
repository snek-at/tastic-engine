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

    # Get all issues
    def getIssues(self, repos):
        issues = []

        # Loop through each found repository
        for repo in repos:
            # Get all issues from the repository
            with requests.get(
                f"{self.api_url}/repos/snek-at/{repo}/issues?state=all&access_token={os.getenv('ACCESS_TOKEN')}"
            ) as issue_req:
                # Convert html response to json
                issue_json = json.loads(issue_req.text)

                # Loop through each issue
                for issue in issue_json:
                    # Loop through each label
                    for label in issue["labels"]:
                        # Check if the label is in the defined labels
                        if label["name"] in self.labels:
                            # Get datetime when the issue was created
                            created_at = datetime.strptime(
                                issue["created_at"], "%Y-%m-%dT%H:%M:%SZ"
                            )

                            # Check if issue was created after project start
                            if created_at > self.project_start:

                                # Check if issue is an actual issue and not a pull request
                                if "pull_request" not in issue:
                                    issues.append(issue)

        # Return found issues
        return issues

    # Create calendar
    def determineIssues(self, issues):
        calendar = {}
        today = datetime.today()
        project_start = self.project_start

        while today > project_start:
            calendar[project_start] = []
            project_start += timedelta(days=1)

        # Loop through each date of the calendar
        for date in calendar:
            issues_closed_per_date = {
                "Requirement": 0,
                "Feature": 0,
                "Opportunity": 0,
                "bug": 0,
                "enhancement": 0,
            }

            # Loop through each issue
            for issue in issues:
                # Check if issue was closed
                closed_at = issue["closed_at"]
                if closed_at:
                    closed_at = datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ")
                    # Check if GitHub closed at equals calendar date
                    if (
                        closed_at.year == date.year
                        and closed_at.month == date.month
                        and closed_at.day == date.day
                    ):
                        # Loop through each label
                        for label in self.labels:
                            # Loop through each issue label
                            for issue_label in issue["labels"]:
                                if label == issue_label["name"]:
                                    issues_closed_per_date[label] += 1

            calendar[date] = issues_closed_per_date

        # Return calendar
        return calendar
