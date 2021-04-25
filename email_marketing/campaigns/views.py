from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import Response
from rest_framework.decorators import action

from . import models, serializers
from .forms import ContentForm

def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = models.Campaign.objects.all()
    serializer_class = serializers.CampaignSerializer

    def list(self, request):
        queryset = models.Campaign.objects.all()
        serializer = serializers.ContentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # def get_form(self, request):
    #     form = ContentForm()
        
    #     context = {
    #         'form': form
    #     }

    #     return render(request, 'index/content.html', context)
                



