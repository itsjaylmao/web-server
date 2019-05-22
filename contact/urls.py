from django.contrib import admin
from django.urls import path

from .views import contactView

urlpatterns = [
    path('', contactView, name="contact"),
]
