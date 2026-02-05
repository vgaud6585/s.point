from django.contrib import admin
from .models import StudyRecape
# Register your models here.

@admin.register(StudyRecape)
class StudyRecapeAdmin(admin.ModelAdmin):
	list_display = ['id']