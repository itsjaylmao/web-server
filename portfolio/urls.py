from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('project/<int:pk>/', views.project, name='project'),
]