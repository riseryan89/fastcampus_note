from django.contrib import admin
from django.urls import path

from app.apis import test_api, get_or_create_categories, get_or_create_notes, update_or_delete_note

urlpatterns = [
    path("user_api", test_api),
    path("categories", get_or_create_categories),
    path("notes", get_or_create_notes),
    path("notes/<int:note_id>", update_or_delete_note),
]
