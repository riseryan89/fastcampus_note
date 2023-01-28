from django.contrib import admin
from django.urls import path, include

from app.apis.users_api import test_api
from app import views as v

urlpatterns = [
    path("", v.index, name="index"),
    path("signup", v.user_signup, name="signup"),
    path("signup2", v.user_signup2, name="signup2"),
]
