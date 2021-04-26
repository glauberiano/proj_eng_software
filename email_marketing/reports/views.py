from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import Response
from rest_framework.decorators import action

from . import models, serializers

# Create your views here.

def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = models.Reports.objects.all()
    serializer_class = serializers.ReportSerializer