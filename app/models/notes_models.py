from django.contrib.auth.models import User
from django.db import models

from app.models.abstract_models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=20, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Note(BaseModel):
    title = models.CharField(max_length=256, null=False, db_index=True)
    content = models.TextField(null=True)
    image = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notes"
        indexes = [
            models.indexes.Index(fields=["title", "is_deleted"], name="ix_notes_title_is_deleted"),
        ]
