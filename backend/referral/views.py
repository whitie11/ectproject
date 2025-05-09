from datetime import date, datetime
from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from rest_framework import status
from referral import serializers
from patient.models import Patient
from referral.models import Referral, ReferralStage
from referral.serializers import ReferralSerializer
from progress_notes.serializers import ProgressNotesSerializer

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
        # patient_id = request.data.get('patient_id')
        # patient = Patient.objects.get(pk=patient_id)
        newReferral = {
            'patient_id': request.data.get('patient_id'),
            'referrer': request.data.get("referrer"),
            'referrer_email': request.data.get("referrer_email"),
            'reason': request.data.get("reason"),
        }

        serializer = ReferralSerializer(data=newReferral)
        if serializer.is_valid():
            serializer.save()
            newNote = {
                'referral_id': serializer.data.get('referral_id'),
                'author_id': request.data.get('author_id'),
                'note': "New referal made"
            }
            noteSerializer = ProgressNotesSerializer(data=newNote)
            if noteSerializer.is_valid():
                noteSerializer.save()
            else:
                return JsonResponse(noteSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReferralUpdateStage(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        referral_Id = request.data.get('referral_Id')
        author_id = request.data.get('author_id')
        stage = request.data.get('stage')
        notes = request.data.get('notes')
        referral = Referral.objects.get(pk=referral_Id)

        referral.stage = stage
        if stage == "CP":
            referral.isOpen = False
            referral.date_closed = datetime.now()
        referral.save()

        str = referral.get_stage_display()

        newNote = {
            'referral_id': referral_Id,
            'author_id': author_id,
            'note': "Stage updated to " + str + "\n" + notes
        }
        noteSerializer = ProgressNotesSerializer(data=newNote)
        if noteSerializer.is_valid():
            noteSerializer.save()
        else:
            return JsonResponse(noteSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(noteSerializer.data, status=status.HTTP_201_CREATED)
