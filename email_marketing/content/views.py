from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.views import Response
from rest_framework.decorators import action
from django.http import Http404
from operator import itemgetter


from . import models, serializers


class ContentViewSet(viewsets.ModelViewSet):
    queryset = models.Campaign.objects.all()
    serializer_class = serializers.ContentSerializer

    def list(self, request):
        queryset = models.Campaign.objects.all()
        serializer = serializers.ContentSerializer(queryset, many=True)
        return Response(serializer.data)

