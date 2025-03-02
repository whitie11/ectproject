from django.contrib import admin
from .models import ProgressNote


class ProgressNoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProgressNote, ProgressNoteAdmin)
