from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("login/", login_page, name="login_page"),
    path("register/", register_page, name="register_page"),
    path("user_logout/", user_logout, name="user_logout"),
    path("profile/",profile_page, name="profile_page"),
]