from django.shortcuts import render
from rest_framework import viewsets
from .models import switchhost 
from .serializers import DeviceSerializer
# Create your views here.

class deviceview(viewsets.ModelViewSet):
   # queryset=Role.objects.all()
    queryset1=switchhost.objects.all()
    serializer_class = DeviceSerializer

