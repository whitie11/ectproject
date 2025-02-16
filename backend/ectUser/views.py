from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import EctUserSerializer

# Create your views here.
User = get_user_model()


class EctUser(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        userID = request.query_params.get('userId')
        if userID:
            user = User.objects.get(pk=userID)
            serialiser = EctUserSerializer(user, many=False, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)
        else:
            user_all = User.objects.all()
            serialiser = EctUserSerializer(user_all, many=True, context={'request': request})
            return JsonResponse(serialiser.data, safe=False)
