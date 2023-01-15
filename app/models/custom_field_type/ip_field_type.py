import socket

from django.core.exceptions import ValidationError
from django.db import models


class IPAddressField(models.Field):
    description = "IPv4 또는 IPv6 주소 필드"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 39
        super().__init__(*args, **kwargs)

    def check_ip(self, value):
        try:
            socket.inet_pton(socket.AF_INET6, value)
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET, value)
            except socket.error:
                raise ValidationError("Invalid IP address.")

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        if value is None:
            return value
        self.check_ip(value)
        return value

    def get_prep_value(self, value):
        self.check_ip(value)
        return value

    def get_internal_type(self):
        return "CharField"
