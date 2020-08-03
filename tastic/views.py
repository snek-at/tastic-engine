from django.shortcuts import render


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