from rest_framework import serializers
from contacts import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contacts
        fields = "__all__"