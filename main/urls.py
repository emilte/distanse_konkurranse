"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('forbidden/', TemplateView.as_view(template_name="main/forbidden.html"), name='forbidden'),
    path('admin/', admin.site.urls),
    path('distanse/', include('distance.urls')),
    path('emil/', include('emil.urls')),
    path('henrik/', include('henrik.urls')),
    path('patrick/', include('patrick.urls')),
    path('stefan/', include('stefan.urls')),
    path('accounts/', include('accounts.urls')),
]
