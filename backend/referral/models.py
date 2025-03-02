from django.db import models
from datetime import date, datetime

from patient.models import Patient

# Create your models here.


class ReferralStage(models.TextChoices):
    PENDING = "PD", "Pending review"
    NOT_ALOCATED = "WL", "On waiting list"
    DECLINED = "DX", "Declined"
    CLOSED = "CL", "Closed"
    ACCEPTED_P = "AP", "Accepted Preston"
    ACCEPTED_B = "AB", "Accepted Blackburn"
    TREATMENT_P = "TP", "Treatment Preston"
    TREATMENT_B = "TB", "Treatment Blackburn"
    COMPLETED = "CP", "Completed"


class Referral(models.Model):
    referral_id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.RESTRICT)
    referrer = models.CharField(max_length=20)
    referrer_email = models.CharField(max_length=50)
    reason = models.TextField()
    stage = models.CharField(max_length=2, choices=ReferralStage.choices, default=ReferralStage.PENDING)
    isOpen = models.BooleanField(default=True)
    date_started = models.DateField(default=date.today)
    date_closed = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name}: {ReferralStage(self.stage).label}"


# class ReferralTemp(models.Model):
#     referral_id = models.BigAutoField(primary_key=True)
#     patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
#     referrer = models.CharField(max_length=20)
#     referrer_email = models.CharField(max_length=50)
#     reason = models.TextField()
#     stage = models.CharField(max_length=2, choices=ReferralStage.choices, default=ReferralStage.PENDING)
#     isOpen = models.BooleanField(default=True)
#     date_started = models.DateField(default=date.today)
#     date_closed = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.patient.first_name} {self.patient.last_name}: {ReferralStage(self.stage).label}"


# class ReferralTemp2(models.Model):
#     referral_id = models.BigAutoField(primary_key=True)
#     patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
#     referrer = models.CharField(max_length=20)
#     referrer_email = models.CharField(max_length=50)
#     reason = models.TextField()
#     stage = models.CharField(max_length=2, choices=ReferralStage.choices, default=ReferralStage.PENDING)
#     isOpen = models.BooleanField(default=True)
#     date_started = models.DateField(default=date.today)
#     date_closed = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.patient.first_name} {self.patient.last_name}: {ReferralStage(self.stage).label}"
