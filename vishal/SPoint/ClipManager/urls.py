from django.urls import path
from . import views

urlpatterns = [
    path('clip-show/', views.clip_show, name='clip_home'),
    path('clip-add/', views.clip_add, name='clip_add'),
    path('edit/<int:pk>/', views.clip_edit, name='clip_edit'),
    path('delete/<int:pk>/', views.clip_delete, name='clip_delete'),
]
