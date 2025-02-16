from django.db import models

# Create your models here.


class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    UNSPECIFIED = "U", "Unspecified"


class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(blank=True, max_length=50)
    date_of_birth = models.DateField()
    nhs_no = models.CharField(max_length=10, unique=True)
    gender = models.CharField(blank=True, choices=Gender.choices, max_length=2, default=Gender.UNSPECIFIED)

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} NHS:{self.nhs_no}"
