from requests import request
from rest_framework import serializers
from referral.models import Referral
from referral.serializers import ReferralSerializer
from progress_notes.models import ProgressNote
from ectUser.models import EctUser
from ectUser.serializers import EctUserSerializer


class ProgressNotesSerializer(serializers.ModelSerializer):
    referral = ReferralSerializer(read_only=True)
    referral_id = serializers.PrimaryKeyRelatedField(
        source="referral",
        queryset=Referral.objects.all())
    author = EctUserSerializer(read_only=True, required=False)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=EctUser.objects.all(),
        allow_null=True,
    )

    class Meta:
        model = ProgressNote
        fields = (
            "note_id",
            "note",
            "date_created",
            "referral_id",
            "referral",
            "author_id",
            "author",
        )
        depth = 1
