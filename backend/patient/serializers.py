from rest_framework import serializers

from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    # gender = serializers.CharField(source="get_gender_display")

    class Meta:
        model = Patient
        fields = ('__all__')
