from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from client.main import githubClient
from tastic.models import Throughput, BurnDown, Features, Dods, Stories, Reports

from datetime import *

# Global variables
client = githubClient(
    labels=["Feature", "Opportunity", "Requirement", "bug", "enhancement"]
)
filters = [
    {"id": 1, "name": "All time", "selected": False},
    {"id": 2, "name": "Last Year", "selected": False},
    {"id": 3, "name": "Last Month", "selected": False},
    {"id": 4, "name": "Last Week", "selected": False},
    {"id": 5, "name": "Last Day", "selected": False},
]

# This function should be executed daily using a cronjob
def getData():
    global client

    # Throughput
    repos = client.getRepositories()
    issues = client.getIssues(repos)
    calendar = client.determineIssues(issues)
    update_throughput(calendar)
    barData = client.getThroughput(calendar)

    # Burndown
    projects = client.getProjects()
    columns = client.getColumns(projects)
    cards = client.getCards(columns)
    calendar = client.determineCards(cards)
    update_burnDown(calendar)
    lineData = client.getBurndown(calendar)

    # Get features file
    features = client.getFeatures(issues)
    path, filename = client.issuesToPDFs(issues=features, name="features")
    update_features(path, filename)

    # Get definition of done file
    opportunities = client.getOpportunities(issues)
    path, filename = client.issuesToPDFs(issues=opportunities, name="dods")
    update_dods(path, filename)

    # Get user stories
    path, filename = client.getUserStories(features=features, name="stories")
    update_stories(path, filename)


def update_features(path, filename):
    try:
        features = Features.objects.get(filename=filename)
    except Features.DoesNotExist:
        features = Features()
        features.filename = filename

    features.path = path
    features.save()


def get_features():
    files = []

    for feature in Features.objects.all():
        files.append(
            {"name": feature.filename, "createdAt": feature.date,}
        )

    files.reverse()
    return files


def update_dods(path, filename):
    try:
        dods = Dods.objects.get(filename=filename)
    except Dods.DoesNotExist:
        dods = Dods()
        dods.filename = filename

    dods.path = path
    dods.save()


def get_dods():
    files = []

    for dod in Dods.objects.all():
        files.append(
            {"name": dod.filename, "createdAt": dod.date,}
        )

    files.reverse()
    return files


def update_stories(path, filename):
    try:
        stories = Stories.objects.get(filename=filename)
    except Stories.DoesNotExist:
        stories = Stories()
        stories.filename = filename

    stories.path = path
    stories.save()


def get_stories():
    files = []

    for story in Stories.objects.all():
        files.append(
            {"name": story.filename, "createdAt": story.date,}
        )

    files.reverse()
    return files


def update_reports(path, filename, owner):
    try:
        reports = Reports.objects.get(filename=filename)
    except Reports.DoesNotExist:
        reports = Reports()
        reports.filename = filename

    reports.path = path
    reports.owner = owner
    reports.save()


def get_reports():
    reports = []

    for user in User.objects.all():
        if user.username != "admin":
            files = []

            for file in Reports.objects.filter(owner=user):
                files.append({"name": file.filename, "createdAt": file.date})

            files.reverse()
            reports.append({"owner": user, "files": files})

    return reports


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


def get_burnDown():
    global client

    calendar = {}

    for burnDown in BurnDown.objects.all():
        calendar[burnDown.date] = {
            "actual": burnDown.actual,
            "ideal": burnDown.ideal,
        }

    return client.getBurndown(calendar)


def get_year_burnDown():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=365)

    for burnDown in BurnDown.objects.filter(date__range=[startdate, enddate]):
        calendar[burnDown.date] = {
            "actual": burnDown.actual,
            "ideal": burnDown.ideal,
        }

    return client.getBurndown(calendar)


def get_month_burnDown():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=31)

    for burnDown in BurnDown.objects.filter(date__range=[startdate, enddate]):
        calendar[burnDown.date] = {
            "actual": burnDown.actual,
            "ideal": burnDown.ideal,
        }

    return client.getBurndown(calendar)


def get_week_burnDown():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=7)

    for burnDown in BurnDown.objects.filter(date__range=[startdate, enddate]):
        calendar[burnDown.date] = {
            "actual": burnDown.actual,
            "ideal": burnDown.ideal,
        }

    return client.getBurndown(calendar)


def get_day_burnDown():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=1)

    for burnDown in BurnDown.objects.filter(date__range=[startdate, enddate]):
        calendar[burnDown.date] = {
            "actual": burnDown.actual,
            "ideal": burnDown.ideal,
        }

    return client.getBurndown(calendar)


def update_throughput(calendar):
    for date in calendar:
        try:
            throughput = Throughput.objects.get(date=date)
        except Throughput.DoesNotExist:
            throughput = Throughput()
            throughput.date = date

        date = calendar[date]
        throughput.features = date["Feature"]
        throughput.requirements = date["Requirement"]
        throughput.opportunities = date["Opportunity"]
        throughput.enhancements = date["enhancement"]
        throughput.bugs = date["bug"]
        throughput.save()


def get_throughput():
    global client

    calendar = {}

    for throughput in Throughput.objects.all():
        calendar[throughput.date] = {
            "Feature": throughput.features,
            "Requirement": throughput.requirements,
            "Opportunity": throughput.opportunities,
            "enhancement": throughput.enhancements,
            "bug": throughput.bugs,
        }

    return client.getThroughput(calendar)


def get_year_throughput():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=365)

    for throughput in Throughput.objects.filter(date__range=[startdate, enddate]):
        calendar[throughput.date] = {
            "Feature": throughput.features,
            "Requirement": throughput.requirements,
            "Opportunity": throughput.opportunities,
            "enhancement": throughput.enhancements,
            "bug": throughput.bugs,
        }

    return client.getThroughput(calendar)


def get_month_throughput():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=31)

    for throughput in Throughput.objects.filter(date__range=[startdate, enddate]):
        calendar[throughput.date] = {
            "Feature": throughput.features,
            "Requirement": throughput.requirements,
            "Opportunity": throughput.opportunities,
            "enhancement": throughput.enhancements,
            "bug": throughput.bugs,
        }

    return client.getThroughput(calendar)


def get_week_throughput():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=7)

    for throughput in Throughput.objects.filter(date__range=[startdate, enddate]):
        calendar[throughput.date] = {
            "Feature": throughput.features,
            "Requirement": throughput.requirements,
            "Opportunity": throughput.opportunities,
            "enhancement": throughput.enhancements,
            "bug": throughput.bugs,
        }

    return client.getThroughput(calendar)


def get_day_throughput():
    global client

    calendar = {}
    enddate = date.today()
    startdate = enddate - timedelta(days=1)

    for throughput in Throughput.objects.filter(date__range=[startdate, enddate]):
        calendar[throughput.date] = {
            "Feature": throughput.features,
            "Requirement": throughput.requirements,
            "Opportunity": throughput.opportunities,
            "enhancement": throughput.enhancements,
            "bug": throughput.bugs,
        }

    return client.getThroughput(calendar)


def index(request):
    # getData()
    reports = []

    for report in get_reports():
        if report["files"] != []:
            reports.append({"owner": report["owner"], "files": [report["files"][0]]})
        else:
            reports.append(report)

    values = {
        "lineData": get_week_burnDown(),
        "barData": get_week_throughput(),
        "story": get_stories()[0],
        "reports": reports,
        "feature": get_features()[0],
        "dod": get_dods()[0],
    }

    # Render site
    return render(request, "index.html", values)


def features(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "files": get_features(),
    }

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    values["files"] = add_pagination(page, values["files"])

    # Render site
    return render(request, "pages/features.html", values)


def dods(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "files": get_dods(),
    }

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    values["files"] = add_pagination(page, values["files"])

    # Render site
    return render(request, "pages/dods.html", values)


def stories(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "files": get_stories(),
    }

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    values["files"] = add_pagination(page, values["files"])

    # Render site
    return render(request, "pages/stories.html", values)


def reports(request):
    # Dummy Data
    values = {
        "sortedBy": "Newest",
        "reports": get_reports(),
    }

    # Render site
    return render(request, "pages/reports.html", values)


def throughputs(request):
    global filters

    # Dummy data
    values = {"filters": filters, "barData": get_throughput()}

    # Render site
    return render(request, "pages/throughputs.html", values)


def burndowns(request):
    global filters

    # Dummy data
    values = {"filters": filters, "lineData": get_burnDown()}

    # Render site
    return render(request, "pages/burndowns.html", values)


def download_feature(request, filename):
    try:
        feature = Features.objects.get(filename=filename)
        path = feature.path
        res = FileResponse(open(path, "rb"))
        return res
    except Features.DoesNotExist():
        return Http404("File not found")


def download_story(request, filename):
    try:
        story = Stories.objects.get(filename=filename)
        path = story.path
        res = FileResponse(open(path, "rb"))
        return res
    except Features.DoesNotExist():
        return Http404("File not found")


def download_dod(request, filename):
    try:
        dod = Dods.objects.get(filename=filename)
        path = dod.path
        res = FileResponse(open(path, "rb"))
        return res
    except Features.DoesNotExist():
        return Http404("File not found")


def download_report(request, filename):
    try:
        report = Reports.objects.get(filename=filename)
        path = report.path
        res = FileResponse(open(path, "rb"))
        return res
    except Features.DoesNotExist():
        return Http404("File not found")


@login_required
def upload_report(request):
    global client

    if request.method == "POST" and request.FILES["report"]:
        report = request.FILES["report"]
        owner = request.user

        path, filename = client.putReport(report, owner)
        update_reports(path, filename, owner)

        values = {"reports": get_reports()}
        print(values)
        # Render site
        return render(request, "pages/reports.html", values)


def search_features(request):
    values = {}
    files = []

    # Get features from db
    for feature in Features.objects.filter(
        filename__contains=request.POST.get("filename")
    ):
        files.append(
            {"name": feature.filename, "createdAt": feature.date,}
        )

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    values["files"] = add_pagination(page, files)
    values["sortedBy"] = request.POST.get("filter")

    # Render site
    return render(request, "pages/features.html", values)


def search_stories(request):
    values = {}
    files = []

    # Get stories from db
    for story in Stories.objects.filter(
        filename__contains=request.POST.get("filename")
    ):
        files.append(
            {"name": story.filename, "createdAt": story.date,}
        )
    # Add Pagination for files list
    page = request.GET.get("page", 1)

    values["files"] = add_pagination(page, files)
    values["sortedBy"] = request.POST.get("filter")

    # Render site
    return render(request, "pages/stories.html", values)


def search_dods(request):
    values = {}
    files = []

    # Get dods from db
    for dod in Dods.objects.filter(filename__contains=request.POST.get("filename")):
        files.append(
            {"name": dod.filename, "createdAt": dod.date,}
        )

    # Add Pagination for files list
    page = request.GET.get("page", 1)

    values["files"] = add_pagination(page, files)
    values["sortedBy"] = request.POST.get("filter")

    # Render site
    return render(request, "pages/dods.html", values)


def filter_burndowns(request):
    global filters

    updated_filters = []
    selected_id = int(request.POST.get("filter"))

    for item in filters:
        if item["id"] == selected_id:
            item["selected"] = True
        else:
            item["selected"] = False

        updated_filters.append(item)

    filters = updated_filters

    lineData = get_burnDown()

    if selected_id == 2:
        lineData = get_year_burnDown()
    elif selected_id == 3:
        lineData = get_month_burnDown()
    elif selected_id == 4:
        lineData = get_week_burnDown()
    elif selected_id == 5:
        lineData = get_day_burnDown()

    values = {"filters": filters, "lineData": lineData}

    # Render site
    return render(request, "pages/burndowns.html", values)


def filter_throughputs(request):
    global filters

    updated_filters = []
    selected_id = int(request.POST.get("filter"))

    for item in filters:
        if item["id"] == selected_id:
            item["selected"] = True
        else:
            item["selected"] = False

        updated_filters.append(item)

    filters = updated_filters

    barData = get_throughput()

    if selected_id == 2:
        barData = get_year_throughput()
    elif selected_id == 3:
        barData = get_month_throughput()
    elif selected_id == 4:
        barData = get_week_throughput()
    elif selected_id == 5:
        barData = get_day_throughput()

    values = {"filters": filters, "barData": barData}

    # Render site
    return render(request, "pages/throughputs.html", values)


def add_pagination(page, files):
    paginator = Paginator(files, 7)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return files
