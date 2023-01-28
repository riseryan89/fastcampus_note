from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from django.db import models
from app.models.custom_field_type.ip_field_type import IPAddressField

from app.models.abstract_models import BaseModel


# AbstractBaseUser
# AbstractUser
# User


class UserDetail(BaseModel):
    user_detail = models.OneToOneField(User, related_name="user_detail", on_delete=models.CASCADE)
    last_ip = IPAddressField(null=True)  # models.GenericIPAddressField
