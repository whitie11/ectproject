from django.contrib import admin
from .models import ProgressNote


class ProgressNoteAdmin(admin.ModelAdmin):
    fields = ['referral', 'author', 'note', 'date_created']
    readonly_fields = ['date_created']


admin.site.register(ProgressNote, ProgressNoteAdmin)
