from django.contrib import admin

from app import models as m

# Register your models here.
admin.site.register(m.Category)
admin.site.register(m.Note)
admin.site.register(m.UserDetail)
