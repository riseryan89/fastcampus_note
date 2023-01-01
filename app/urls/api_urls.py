from django.contrib import admin
from django.urls import path, include

from app.apis import test_api

urlpatterns = [
    path("user_api", test_api),
]
