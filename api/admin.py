from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.Appointment)
admin.site.register(models.Contact)
admin.site.register(models.Bed)
