from django.contrib import admin
from django.conf.locale.es import formats as es_format

from .models import Patient

# Register your models here.

es_format.DATETIME_FORMAT = "d M Y"


class PatientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)
