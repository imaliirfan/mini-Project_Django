"""
URL configuration for chaiAurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# This the main urls.y file of the project 
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
from . import views
#routing 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('chai/', include('chai.urls')),

    path ("__reload__/", include("django_browser_reload.urls")), # this is used for the auto reload
    # this is not used in the production 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# sometimes we have to transfer the contol to the 
# app urls.py files