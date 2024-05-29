from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from blog.models import BlogList
from blog.serializers import BlogSerializer
from rest_framework import viewsets
from contentmanage.models import ContentList
from blog.models import BlogList

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogList.objects.all()
    serializer_class = BlogSerializer

def index(request):
    #data = ContentList.objects.get(BlockName='Portfolio')
    blogs = BlogList.objects.all()
    return render(request, 'index.html', locals())

