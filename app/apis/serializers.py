from datetime import datetime, date

from django.core.serializers.json import DjangoJSONEncoder


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%m/%d/%Y %H:%M:%S")
        if isinstance(obj, date):
            return obj.strftime("%m/%d/%Y %H:%M:%S")
        return super().default(obj)
