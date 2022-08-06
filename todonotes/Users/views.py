from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserModelSerializer

class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer