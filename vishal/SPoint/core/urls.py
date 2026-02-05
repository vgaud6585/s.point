from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/', views.Dashboard, name="dashboard"),
	path('study-list/', views.study_recap_list, name="study-list"),
	# Edit aur Delete ke liye URLs
  path('recaps/edit/<int:pk>/', views.edit_recap, name='edit_recap'),
  path('recaps/delete/<int:pk>/', views.delete_recap, name='delete_recap'),
]