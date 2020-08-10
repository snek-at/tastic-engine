from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from client.main import githubClient
from tastic.models import Throughput, BurnDown
barData = {}
lineData = {}


def getData():
    global lineData
    global barData

    client = githubClient(
        labels=["Feature", "Opportunity", "Requirement", "bug", "enhancement"]
    )

    # Throughput
    repos = client.getRepositories()
    issues = client.getIssues(repos)
    calendar = client.determineIssues(issues)
    barData = client.getThroughput(calendar)

    # Burndown
    projects = client.getProjects()
    columns = client.getColumns(projects)
    cards = client.getCards(columns)
    calendar = client.determineCards(cards)
    lineData = client.getBurndown(calendar)


def update_burnDown(calendar):
    for date in calendar:
        try:
            burnDown = BurnDown.objects.get(date=date)
        except BurnDown.DoesNotExist:
            burnDown = BurnDown()
            burnDown.date = date

        date = calendar[date]
        burnDown.actual = date["actual"]
        burnDown.ideal = date["ideal"]
        burnDown.save()

def index(request):
    global lineData
    global barData

    # This function will be moved into a cronjob, when the program gets moved into a container
    if lineData == {} or barData == {}:
        getData()
    # determined = client.determineCards(cards, columns)
    # Dummy data
    values = {
        "lineData": lineData,
        "barData": barData,
        "story": {
            "name": "User Story 1",
            "createdAt": "29/07/2020",
            "viewUrl": "https://snek.at",
            "downloadUrl": "https://snek.at",
        },
        "report": {
            "name": "Status Report Pinterid",
            "createdAt": "29/07/2020",
            "viewUrl": "https://snek.at",
            "downloadUrl": "https://snek.at",
        },
        "feature": {
            "name": "Feature Collection 1",
            "createdAt": "29/07/2020",
            "viewUrl": "https://snek.at",
            "downloadUrl": "https://snek.at",
        },
        "dod": {
            "name": "Defintion of Done Sprint 1",
            "createdAt": "29/07/2020",
            "viewUrl": "https://snek.at",
            "downloadUrl": "https://snek.at",
        },
    }

    # Render site
    return render(request, "index.html", values)


def features(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "files": [
            {
                "name": "File1",
                "createdAt": "29/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File2",
                "createdAt": "30/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
        ],
    }

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    paginator = Paginator(values["files"], 7)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    values["files"] = files

    # Render site
    return render(request, "pages/features.html", values)


def dods(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "files": [
            {
                "name": "File1",
                "createdAt": "29/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File2",
                "createdAt": "30/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
        ],
    }

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    paginator = Paginator(values["files"], 7)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    values["files"] = files

    # Render site
    return render(request, "pages/dods.html", values)


def stories(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "files": [
            {
                "name": "File1",
                "createdAt": "29/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File2",
                "createdAt": "30/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
            {
                "name": "File3",
                "createdAt": "31/07/2020",
                "viewUrl": "https://snek.at",
                "downloadUrl": "https://snek.at",
            },
        ],
    }

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    paginator = Paginator(values["files"], 7)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    values["files"] = files

    # Render site
    return render(request, "pages/stories.html", values)


def reports(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "users": [
            {
                "name": "Pinterid",
                "is_authenticated": True,
                "files": [
                    {
                        "name": "File1",
                        "createdAt": "29/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                ],
            },
            {
                "name": "Kleber",
                "is_authenticated": False,
                "files": [
                    {
                        "name": "File1",
                        "createdAt": "29/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                ],
            },
            {
                "name": "Schett",
                "is_authenticated": False,
                "files": [
                    {
                        "name": "File1",
                        "createdAt": "29/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                    {
                        "name": "File2",
                        "createdAt": "30/07/2020",
                        "viewUrl": "https://snek.at",
                        "downloadUrl": "https://snek.at",
                    },
                ],
            },
        ],
    }

    # Render site
    return render(request, "pages/reports.html", values)


def throughputs(request):
    global barData
    # Dummy data
    values = {"filteredBy": "All time", "barData": barData}

    # Render site
    return render(request, "pages/throughputs.html", values)


def burndowns(request):
    global lineData
    # Dummy data
    values = {"filteredBy": "All time", "lineData": lineData}

    # Render site
    return render(request, "pages/burndowns.html", values)
