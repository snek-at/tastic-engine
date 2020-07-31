from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_route"),
    #TODO Views have to be changed if the views get updated
    path('login/', views.index, name='login_route'),
    path('logout/', views.index, name='logout_route'),
    path("throughputs/", views.index, name="throughput_charts_route"),
    path("burndowns/", views.index, name="burn_down_charts_route"),
    path("features/", views.index, name="features_route"),
    path("dods/", views.index, name="dods_route"),
    path("stories/", views.index, name="user_stories_route"),
    path("reports/", views.index, name="status_reports_route"),
]
