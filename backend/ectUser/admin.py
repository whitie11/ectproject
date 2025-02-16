from django.contrib import admin

from .models import EctUser

# Register your models here.


class EctUsrAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'is_active', 'role')
    list_editable = ('email', 'is_active', 'role')


admin.site.register(EctUser, EctUsrAdmin)
