from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<slug:slug>/', views.blog_post, name='blog_post'),
    path('<category>/', views.blog_category, name='blog_category'),
]
