from requests import request
from rest_framework import serializers
from patient.models import Patient
from patient.serializers import PatientSerializer
from referral.models import Referral, ReferralTemp, ReferralTemp2


class ReferralSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source="patient", write_only=True, allow_null=True),
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Referral
        fields = (
            "referral_id",
            "patient",
            "patient_id",
            "referrer",
            "referrer_email",
            "reason",
            "stage",
            "isOpen",
            "date_started",
            "date_closed",
        )
        depth = 1


class ReferralTemp2Serializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source="patient", write_only=True, allow_null=True),

    class Meta:
        model = ReferralTemp2
        fields = (
            "referral_id",
            "patient_id",
            "patient",
            "referrer",
            "referrer_email",
            "reason",
            "stage",
            "isOpen",
            "date_started",
            "date_closed",
        )
        depth = 1
