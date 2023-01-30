from django.contrib import admin
from django.urls import path, include

from app.apis.users_api import test_api
from app import views as v

urlpatterns = [
    path("", v.index, name="index"),
    path("cache_test", v.cache_test, name="cache_test"),
    path("cache_test2", v.cache_test2, name="cache_test2"),
    path("login", v.user_login, name="login"),
    path("logout", v.user_logout, name="logout"),
    path("signup", v.user_signup, name="signup"),
    path("signup2", v.user_signup2, name="signup2"),
]
