from django.shortcuts import render
from rest_framework import viewsets
from .models import Phones
from .serializers import PhonesSerializer
# Create your views here.
class PhonesViewSet(viewsets.ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
