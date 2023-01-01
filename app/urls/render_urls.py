from django.contrib import admin
from django.urls import path, include

from app.apis.users_api import test_api
from app.views import index

urlpatterns = [
    path("", index),
]
