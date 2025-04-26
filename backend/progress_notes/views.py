from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from progress_notes.serializers import ProgressNotesSerializer
from progress_notes.models import ProgressNote

from patient.models import Patient
from referral.models import Referral
from referral.serializers import ReferralSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 1


class ProgressNoteView(APIView, DefaultPagination):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        limit = request.query_params.get('limit')
        if limit:
            self.page_size = limit
        note_id = request.query_params.get('note_id')
        if note_id:
            note = ProgressNote.objects.get(pk=note_id)
            serialiser = ProgressNotesSerializer(note, many=False, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)
        else:
            note_all = ProgressNote.objects.all()
            results = self.paginate_queryset(note_all, request, view=self)
            serialiser = ProgressNotesSerializer(results, many=True, context={'request': request})
            # return JsonResponse(serialiser.data, safe=False)
            return self.get_paginated_response(serialiser.data)


class ProgressNoteViewByReferral(APIView, DefaultPagination):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        limit = request.query_params.get('limit')
        if limit:
            self.page_size = limit
        referral_id = request.query_params.get('referral_id')
        if referral_id:
            note_all = ProgressNote.objects.all()
            referral_note = note_all.filter(referral=referral_id).order_by('-date_created')
            if referral_note:
                results = self.paginate_queryset(referral_note, request, view=self)
                serialiser = ProgressNotesSerializer(results, many=True, context={'request': request})
                # return JsonResponse(serialiser.data, safe=False)
                return self.get_paginated_response(serialiser.data)
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
