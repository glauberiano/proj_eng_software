from rest_framework import serializers
from content import models
from datetime import datetime


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campaign
        fields = "__all__"
