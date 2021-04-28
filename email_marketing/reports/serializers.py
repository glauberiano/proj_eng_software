from rest_framework import serializers
from reports import models

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reports
        fields = "__all__"