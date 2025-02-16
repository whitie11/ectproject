from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from rest_framework import status
from referral import serializers
from patient.models import Patient
from referral.models import Referral
from referral.serializers import ReferralSerializer, ReferralTemp2Serializer

# Create your views here.


class ReferralView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        referral_Id = request.query_params.get('referral_Id')
        if referral_Id:
            referral = Referral.objects.get(pk=referral_Id)
            serialiser = ReferralSerializer(referral, many=False, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)
        else:
            referral_all = Referral.objects.all()
            serialiser = ReferralSerializer(referral_all, many=True, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)


class ReferralSave(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        patient_id = request.data.get('patient_id')
        # patient = Patient.objects.get(pk=patient_id)
        newReferral = {
            'patient_id': patient_id,
            'referrer': request.data.get("referrer"),
            'referrer_email': request.data.get("referrer_email"),
            'reason': request.data.get("reason"),
        }

        serializer = ReferralTemp2Serializer(data=newReferral)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
