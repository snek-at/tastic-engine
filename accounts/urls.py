from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.user_login, name="login_route"),
    path("logout/", views.user_logout, name="logout_route"),
]
