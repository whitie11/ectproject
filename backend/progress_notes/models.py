from django.db import models
from datetime import date, datetime

from referral.models import Referral
from ectUser.models import EctUser


class ProgressNote(models.Model):
    notes_id = models.BigAutoField(primary_key=True)
    referral = models.ForeignKey(Referral, related_name='referral', on_delete=models.RESTRICT)
    author = models.ForeignKey(EctUser, related_name='user', on_delete=models.RESTRICT, blank=True, null=True)
    note = models.TextField()
    date_created = models.DateField(default=date.today)
