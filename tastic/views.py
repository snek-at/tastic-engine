from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # Render site
    return render(request, "index.html")


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
    # Dummy data
    values = {
        "filteredBy": "All time",
        "barData": {
            "labels": ["25.07", "26.07", "27.07", "28.07", "29.07", "30.07", "31.07"],
            "datasets": [
                {
                    "label": "Requirements",
                    "data": [1, 1, 1, 1, 1, 1, 1],
                    "backgroundColor": [
                        "rgba(144, 249, 162, 0.5)",
                        "rgba(144, 249, 162, 0.5)",
                        "rgba(144, 249, 162, 0.5)",
                        "rgba(144, 249, 162, 0.5)",
                        "rgba(144, 249, 162, 0.5)",
                        "rgba(144, 249, 162, 0.5)",
                        "rgba(144, 249, 162, 0.5)",
                    ],
                    "borderColor": [
                        "rgba(144, 249, 162, 1)",
                        "rgba(144, 249, 162, 1)",
                        "rgba(144, 249, 162, 1)",
                        "rgba(144, 249, 162, 1)",
                        "rgba(144, 249, 162, 1)",
                        "rgba(144, 249, 162, 1)",
                        "rgba(144, 249, 162, 1)",
                    ],
                    "borderWidth": 2,
                },
                {
                    "label": "Features",
                    "data": [1, 1, 1, 1, 1, 1, 1],
                    "backgroundColor": [
                        "rgba(186, 5, 107, 0.5)",
                        "rgba(186, 5, 107, 0.5)",
                        "rgba(186, 5, 107, 0.5)",
                        "rgba(186, 5, 107, 0.5)",
                        "rgba(186, 5, 107, 0.5)",
                        "rgba(186, 5, 107, 0.5)",
                        "rgba(186, 5, 107, 0.5)",
                    ],
                    "borderColor": [
                        "rgba(186, 5, 107, 1)",
                        "rgba(186, 5, 107, 1)",
                        "rgba(186, 5, 107, 1)",
                        "rgba(186, 5, 107, 1)",
                        "rgba(186, 5, 107, 1)",
                        "rgba(186, 5, 107, 1)",
                        "rgba(186, 5, 107, 1)",
                    ],
                    "borderWidth": 2,
                },
                {
                    "label": "Opportunities",
                    "data": [1, 1, 1, 1, 1, 1, 1],
                    "backgroundColor": [
                        "rgba(89, 59, 165, 0.5)",
                        "rgba(89, 59, 165, 0.5)",
                        "rgba(89, 59, 165, 0.5)",
                        "rgba(89, 59, 165, 0.5)",
                        "rgba(89, 59, 165, 0.5)",
                        "rgba(89, 59, 165, 0.5)",
                        "rgba(89, 59, 165, 0.5)",
                    ],
                    "borderColor": [
                        "rgba(89, 59, 165, 1)",
                        "rgba(89, 59, 165, 1)",
                        "rgba(89, 59, 165, 1)",
                        "rgba(89, 59, 165, 1)",
                        "rgba(89, 59, 165, 1)",
                        "rgba(89, 59, 165, 1)",
                        "rgba(89, 59, 165, 1)",
                    ],
                    "borderWidth": 2,
                },
                {
                    "label": "Enhancements",
                    "data": [1, 1, 1, 1, 1, 1, 1],
                    "backgroundColor": [
                        "rgba(162, 238, 239, 0.5)",
                        "rgba(162, 238, 239, 0.5)",
                        "rgba(162, 238, 239, 0.5)",
                        "rgba(162, 238, 239, 0.5)",
                        "rgba(162, 238, 239, 0.5)",
                        "rgba(162, 238, 239, 0.5)",
                        "rgba(162, 238, 239, 0.5)",
                    ],
                    "borderColor": [
                        "rgba(162, 238, 239, 1)",
                        "rgba(162, 238, 239, 1)",
                        "rgba(162, 238, 239, 1)",
                        "rgba(162, 238, 239, 1)",
                        "rgba(162, 238, 239, 1)",
                        "rgba(162, 238, 239, 1)",
                        "rgba(162, 238, 239, 1)",
                    ],
                    "borderWidth": 2,
                },
                {
                    "label": "Bugs",
                    "data": [1, 1, 1, 1, 1, 1, 1],
                    "backgroundColor": [
                        "rgba(215, 58, 74, 0.5)",
                        "rgba(215, 58, 74, 0.5)",
                        "rgba(215, 58, 74, 0.5)",
                        "rgba(215, 58, 74, 0.5)",
                        "rgba(215, 58, 74, 0.5)",
                        "rgba(215, 58, 74, 0.5)",
                        "rgba(215, 58, 74, 0.5)",
                    ],
                    "borderColor": [
                        "rgba(215, 58, 74, 1)",
                        "rgba(215, 58, 74, 1)",
                        "rgba(215, 58, 74, 1)",
                        "rgba(215, 58, 74, 1)",
                        "rgba(215, 58, 74, 1)",
                        "rgba(215, 58, 74, 1)",
                        "rgba(215, 58, 74, 1)",
                    ],
                    "borderWidth": 2,
                },
            ],
        },
    }
    }
