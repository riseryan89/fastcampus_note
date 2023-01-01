from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# AbstractBaseUser
# AbstractUser
# User


# class User(AbstractUser):
#     additional_info_1 = models.CharField(max_length=20, default="")
#     additional_info_2 = models.CharField(max_length=20, null=True)


class Category(models.Model):
    name = models.CharField(max_length=20, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
