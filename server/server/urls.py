"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path
from blog.views import BlogViewSet, index
from contentmanage.views import ContentViewSet, TDKViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'blog', BlogViewSet, basename='common')
router.register(r'content', ContentViewSet, basename='common2')
router.register(r'tdk', TDKViewSet, basename='common3')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path(r'api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
