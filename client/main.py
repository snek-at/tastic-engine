# IMPORTS
import requests
import json
from datetime import *
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import pdfkit
from PyPDF2 import PdfFileReader, PdfFileWriter
import yaml
import shutil

# Class
class githubClient:
    def __init__(
        self,
        labels,
        api_url="https://api.github.com",
        org="snek-at",
        project_start=datetime(2020, 7, 15),
    ):
        # VARIABLES
        project_folder = os.path.expanduser("./")
        load_dotenv(os.path.join(project_folder, ".env"))
        self.api_url = api_url
        self.labels = labels
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

                                    # Prevent duplicates
                                    if issue not in issues:
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

    # Convert calendar data to charts.js data
    def getThroughput(self, calendar):
        labels = []
        feature = {
            "label": "Feature",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }
        requirement = {
            "label": "Requirement",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }
        opportunity = {
            "label": "Opportunity",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }
        bug = {
            "label": "Bug",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }
        enhancement = {
            "label": "Enhancement",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }

        for date in calendar:
            labels.append(f"{date.day}.{date.month}")

            date = calendar[date]
            # Feature
            feature["data"].append(date["Feature"])
            feature["backgroundColor"].append("rgba(186, 5, 107, 0.5)")
            feature["borderColor"].append("rgba(186, 5, 107, 1)")
            # Requirement
            requirement["data"].append(date["Requirement"])
            requirement["backgroundColor"].append("rgba(144, 249, 162, 0.5)")
            requirement["borderColor"].append("rgba(144, 249, 162, 1)")
            # Opportunity
            opportunity["data"].append(date["Opportunity"])
            opportunity["backgroundColor"].append("rgba(89, 59, 165, 0.5)")
            opportunity["borderColor"].append("rgba(89, 59, 165, 1)")
            # Bug
            bug["data"].append(date["bug"])
            bug["backgroundColor"].append("rgba(215, 58, 74, 0.5)")
            bug["borderColor"].append("rgba(215, 58, 74, 1)")
            # Enhancement
            enhancement["data"].append(date["enhancement"])
            enhancement["backgroundColor"].append("rgba(162, 238, 239, 0.5)")
            enhancement["borderColor"].append("rgba(162, 238, 239, 1)")

        datasets = [feature, requirement, opportunity, bug, enhancement]

        chart = {"labels": labels, "datasets": datasets}

        # Return chart data
        return chart

    def getProjects(self):
        projects = []
        # Header for api preview period
        headers = {"Accept": "application/vnd.github.inertia-preview+json"}

        with requests.get(
            f"{self.api_url}/orgs/snek-at/projects?access_token={os.getenv('ACCESS_TOKEN')}",
            headers=headers,
        ) as projects_req:
            # Convert html response to json
            projects_json = json.loads(projects_req.text)

            for project in projects_json:
                if "Sprint" in project["name"]:
                    projects.append(project)

        return projects

    def getColumns(self, projects):
        columns = {}
        # Header for api preview period
        headers = {"Accept": "application/vnd.github.inertia-preview+json"}

        for project in projects:
            with requests.get(
                f"{project['columns_url']}?access_token={os.getenv('ACCESS_TOKEN')}",
                headers=headers,
            ) as columns_req:
                columns_json = json.loads(columns_req.text)
                columns[project["name"]] = columns_json

        return columns

    def getCards(self, columns):
        cards = {}
        # Header for api preview period
        headers = {"Accept": "application/vnd.github.inertia-preview+json"}

        for column in columns:
            column = columns[column]
            for line in column:
                with requests.get(
                    f"{line['cards_url']}?access_token={os.getenv('ACCESS_TOKEN')}&per_page=100",
                    headers=headers,
                ) as cards_req:
                    cards[line["name"]] = json.loads(cards_req.text)

        return cards

    def determineCards(self, cards, sprintDays=20):
        allHours = 0
        ideal = 0
        calendar = {}
        today = datetime.today()
        project_start = self.project_start

        for line in cards:
            for card in cards[line]:
                time = int(card["note"].split("***Duration***\r\n")[1][:1])
                allHours += time

        ideal = allHours
        actual = allHours

        while today > project_start:
            calendar[project_start] = []
            project_start += timedelta(days=1)

        # Loop through each date of the calendar
        for date in calendar:
            time_per_date = {"actual": actual, "ideal": ideal}

            if date.weekday() < 5:
                ideal -= allHours / sprintDays
                if ideal < 0:
                    ideal = 0

            for card in cards["DONE"]:
                updated_at = datetime.strptime(card["updated_at"], "%Y-%m-%dT%H:%M:%SZ")

                if (
                    updated_at.year == date.year
                    and updated_at.month == date.month
                    and updated_at.day == date.day
                ):
                    actual -= int(card["note"].split("***Duration***\r\n")[1][:1])
                    time_per_date["actual"] = actual

            calendar[date] = time_per_date

        return calendar

    # Convert calendar data to charts.js data
    def getBurndown(self, calendar):
        labels = []
        ideal = {
            "label": "Ideal time remaining",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }
        actual = {
            "label": "Actual time remaining",
            "data": [],
            "backgroundColor": [],
            "borderColor": [],
            "borderWidth": 2,
        }

        for date in calendar:
            labels.append(f"{date.day}.{date.month}")

            date = calendar[date]
            # Ideal
            ideal["data"].append(round(date["ideal"]))
            ideal["backgroundColor"].append("rgba(0, 230, 64, 0.5)")
            ideal["borderColor"].append("rgba(0, 230, 64, 1)")
            # Actual
            actual["data"].append(round(date["actual"]))
            actual["backgroundColor"].append("rgba(240, 52, 52, 0.5)")
            actual["borderColor"].append("rgba(240, 52, 52, 1)")

        datasets = [ideal, actual]

        chart = {"labels": labels, "datasets": datasets}

        # Return chart data
        return chart

    def getFeatures(self, issues):
        features = []

        # Filter issues for Feature tag
        for issue in issues:
            for label in issue["labels"]:
                if label["name"] == "Feature":
                    features.append(issue)

        return features

    def getOpportunities(self, issues):
        opportunities = []

        # Filter issues for Feature tag
        for issue in issues:
            for label in issue["labels"]:
                if label["name"] == "Opportunity":
                    opportunities.append(issue)

        return opportunities

    # Convert issues to pdfs
    def issuesToPDFs(self, issues, name):
        files = []
        data = []

        # Loop through each issue
        for issue in issues:
            # Get the html code of the issue
            with requests.get(issue["html_url"]) as html_req:
                # Parse the html code with BeautifulSoup
                soup = BeautifulSoup(html_req.text, "html.parser")
                # Get the head of the html code
                head = soup.findAll("head")[0]
                # Get the class with name edit-comment-hide
                content = soup.find(class_="edit-comment-hide")
                # Combine the head and the issue
                html = f"{str(head)}<body>{str(content)}</body><div style = 'display:block; clear:both; page-break-after:always;'></div>"
                # Create path
                path = f"files/{name}/{issue['title'].replace(' ', '')}"
                os.makedirs(path, exist_ok=True)

                # Create pdf file out of html
                pdfkit.from_string(html, f"{path}/0.pdf")
                output_folder_path = os.path.join(os.getcwd(), path)
                pdf = PdfFileReader(f"{path}/0.pdf")

                # Loop through each page of the default pdf
                for page_num in range(pdf.numPages):
                    pdfWriter = PdfFileWriter()
                    pdfWriter.addPage(pdf.getPage(page_num))

                    # Save each page as a single file
                    with open(
                        os.path.join(output_folder_path, f"{page_num+1}.pdf"), "wb"
                    ) as f:
                        files.append(
                            os.path.join(
                                output_folder_path, f"{page_num+1}.pdf"
                            ).replace("\\", "/")
                        )
                        pdfWriter.write(f)
                        f.close()

                data.append({"title": issue["title"], "files": files})

        # Create yaml file
        yaml_data = yaml.dump(
            {
                "issues": data,
                "filename": name,
                "logo": (os.path.join(os.getcwd(), "media/logo.png")).replace(
                    "\\", "/"
                ),
            }
        )

        with open(os.path.join(f"files/{name}", f"{name}.md"), "w") as f:
            f.write(f"---\n{yaml_data}\n---")
            f.close()

        # Return path and filename for db
        path, filename = self.combinePDFs(name)

        return path, filename

    def getUserStories(self, features, name="stories"):
        stories = []

        # Loop through each feature
        for feature in features:
            stories.append(
                {
                    "title": feature["title"],
                    "text": feature["body"].split("\r\n")[1].replace("- ", ""),
                }
            )

        # Create path
        os.makedirs(os.path.join(f"files/{name}"), exist_ok=True)

        # Create yaml file
        yaml_data = yaml.dump(
            {
                "stories": stories,
                "logo": (os.path.join(os.getcwd(), "media/logo.png")).replace(
                    "\\", "/"
                ),
            }
        )

        with open(os.path.join(f"files/{name}", f"{name}.md"), "w") as f:
            f.write(f"---\n{yaml_data}\n---")
            f.close()

        # Create filename
        today = date.today()
        today = f"{today.year}{today.month}{today.day}.pdf"

        # Create PDF
        os.system(
            f"pandoc -s {os.path.join('files/' + name, name + '.md')} -o {os.path.join('files/' +  name , today)} --from markdown --template stories"
        )

        # Remove unneeded files
        os.remove(os.path.join("files/" + name, name + ".md"))

        # Return path and filename for db
        path = os.path.join(f"files/{name}", today)
        filename = today

        return path, filename

    # Put the singel pdfs into the SNEK template
    def combinePDFs(self, name):
        # Create filename
        today = date.today()
        today = f"{today.year}{today.month}{today.day}.pdf"

        # Create PDF
        os.system(
            f"pandoc -s {os.path.join('files/' + name, name + '.md')} -o {os.path.join('files/' +  name , today)} --from markdown --template snek"
        )

        # Delete unneeded PDFs
        for path in os.listdir(os.path.join(os.getcwd(), f"files/{name}")):
            path = os.path.join(os.getcwd(), f"files/{name}/{path}")
            if os.path.isdir(path):
                shutil.rmtree(path)

        os.remove(os.path.join("files/" + name, name + ".md"))

        # Return path and filename for db
        path = os.path.join(f"files/{name}", today)
        filename = today

        return path, filename

    def putReport(self, report, owner="Pinterid"):
        path = f"files/reports/{owner}"
        os.makedirs(path, exist_ok=True)

        with open(f"{path}/{report.name}", "wb") as file:
            for chunk in report.chunks():
                file.write(chunk)
