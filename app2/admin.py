from django.contrib import admin
from app2.models import table
from app2.models import CustomUser
# Register your models here.
admin.site.register(table)
admin.site.register(CustomUser)
