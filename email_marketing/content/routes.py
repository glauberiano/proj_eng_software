from django.urls import include, path
from rest_framework.routers import DefaultRouter

from content import views

routers = DefaultRouter()
routers.register("content", views.ContentViewSet)

urlpatterns = [path("", include(routers.urls))]