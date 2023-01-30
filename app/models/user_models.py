from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from django.db import models
from app.models.custom_field_type.ip_field_type import IPAddressField

from app.models.abstract_models import BaseModel


# AbstractBaseUser
# AbstractUser
# User


class UserDetail(BaseModel):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    note_count = models.IntegerField(default=0)

    def increase_count(self):
        self.note_count += 1
        self.save()
