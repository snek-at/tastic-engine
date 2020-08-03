from django.shortcuts import render


def index(request):
    # Render site
    return render(request, "index.html")
