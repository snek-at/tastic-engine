from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_route"),
    # TODO Views have to be changed if the views get updated
    path("login/", views.index, name="login_route"),
    path("logout/", views.index, name="logout_route"),
    path("throughputs/", views.throughputs, name="throughput_charts_route"),
    path(
        "throughputs/filter",
        views.filter_throughputs,
        name="filter_throughputs_charts_route",
    ),
    path("burndowns/", views.burndowns, name="burn_down_charts_route"),
    path(
        "burndowns/filter", views.filter_burndowns, name="filter_burn_down_charts_route"
    ),
    path("features/", views.features, name="features_route"),
    path(
        "features/download/<filename>",
        views.dowload_feature,
        name="download_feature_route",
    ),
    path("features/search/", views.search_features, name="search_features_route"),
    path("dods/", views.dods, name="dods_route"),
    path("dods/download/<filename>", views.dowload_dod, name="download_dod_route"),
    path("dods/search/", views.search_dods, name="search_dods_route"),
    path("stories/", views.stories, name="user_stories_route"),
    path("stories/search/", views.search_stories, name="search_stories_route"),
    path(
        "stories/download/<filename>",
        views.dowload_story,
        name="download_stories_route",
    ),
    path("reports/", views.reports, name="status_reports_route"),
]
