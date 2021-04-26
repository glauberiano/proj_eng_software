from django.db.models import fields
from rest_framework import serializers
from campaigns import models


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campaign
        fields = "__all__"

