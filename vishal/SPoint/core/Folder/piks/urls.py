from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery_home'),
    path('serve-image/', views.serve_image, name='serve_image'),
    path('save-note/', views.save_note, name='save_note'),
    path('notes/', views.notes_list_view, name='notes_list'),

]
