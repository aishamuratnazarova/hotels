from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from trivago.viewsets import VisitorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("trivago.urls")),
    path('accounts/', include('allauth.urls')),

]
