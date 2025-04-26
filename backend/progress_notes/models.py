from django.db import models
from datetime import date, datetime

from referral.models import Referral
from ectUser.models import EctUser


class ProgressNote(models.Model):
    note_id = models.BigAutoField(primary_key=True)
    referral = models.ForeignKey(Referral, related_name='referral', on_delete=models.RESTRICT)
    author = models.ForeignKey(EctUser, related_name='user', on_delete=models.RESTRICT, blank=True, null=True)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.note_id} author:{self.author} date:{self.date_created}"
