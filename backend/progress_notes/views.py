from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from rest_framework import status
from progress_notes.serializers import ProgressNotesSerializer
from progress_notes.models import ProgressNote

from patient.models import Patient
from referral.models import Referral
from referral.serializers import ReferralSerializer


class ProgressNoteView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        note_id = request.query_params.get('note_id')
        if note_id:
            note = ProgressNote.objects.get(pk=note_id)
            serialiser = ProgressNotesSerializer(note, many=False, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)
        else:
            note_all = ProgressNote.objects.all()
            serialiser = ProgressNotesSerializer(note_all, many=True, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)


class ProgressNoteViewByReferral(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        referral_id = request.query_params.get('referral_id')
        if referral_id:
            note_all = ProgressNote.objects.all()
            referral_note = note_all.filter(referral=referral_id)
            if referral_note:
                serialiser = ProgressNotesSerializer(referral_note, many=True, context={'request': request})
                return JsonResponse(serialiser.data, safe=False)
            else:
                return JsonResponse({}, status=status. HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({}, status=status.HTTP_400_BAD_REQUEST)


class ProgressNoteSave(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # patient_id = request.data.get('patient_id')
        # patient = Patient.objects.get(pk=patient_id)
        newNote = {
            'referral_id': request.data.get('referral_id'),
            'author_id': request.data.get('author_id'),
            'note': request.data.get('progress_note'),
        }

        serializer = ProgressNotesSerializer(data=newNote)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
