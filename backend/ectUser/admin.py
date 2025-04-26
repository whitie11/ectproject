from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import EctUser

# Register your models here.


class EctUsrAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'is_active', 'role')
    list_editable = ('email', 'is_active', 'role')


admin.site.register(EctUser, EctUsrAdmin)
