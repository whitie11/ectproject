from django.contrib import admin

from .models import Referral

# Register your models here.


class ReferralAdmin(admin.ModelAdmin):
    pass


admin.site.register(Referral, ReferralAdmin)
