from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from patient.models import Patient
from patient.serializers import PatientSerializer


# Create your views here.


class PatientView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        patient_Id = request.query_params.get('patient_id')
        if patient_Id:
            patient = Patient.objects.get(pk=patient_Id)
            serialiser = PatientSerializer(
                patient, many=False, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)
        else:
            patient_all = Patient.objects.all()
            serialiser = PatientSerializer(
                patient_all, many=True, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)


class PatientSave(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = {
            'patient_id': request.data.get("patient_id"),
            'first_name': request.data.get("first_name"),
            'last_name': request.data.get("last_name"),
            'middle_name': request.data.get("middle_name"),
            'date_of_birth': request.data.get("date_of_birth"),
            'nhs_no': request.data.get("nhs_no"),
            'gender': request.data.get("gender"),
        }

        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class PatientSearch(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        search_term = request.query_params.get('search')
        patient_filtered = Patient.objects.filter(first_name__istartswith=search_term).values() \
            | Patient.objects.filter(middle_name__istartswith=search_term).values() \
            | Patient.objects.filter(last_name__istartswith=search_term).values()
        serialiser = PatientSerializer(
            patient_filtered, many=True, context={'request': request})
        return JsonResponse(serialiser.data, safe=False)
