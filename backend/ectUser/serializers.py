from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class EctUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'role']
