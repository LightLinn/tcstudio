from django.shortcuts import render

# Create your views here.
from contentmanage.serializers import ContentSerializer, TDKSerializer
from contentmanage.models import ContentList, TDKList
from rest_framework import viewsets

class ContentViewSet(viewsets.ModelViewSet):
    queryset = ContentList.objects.all()
    serializer_class = ContentSerializer

class TDKViewSet(viewsets.ModelViewSet):
    queryset = TDKList.objects.all()
    serializer_class = TDKSerializer