from django.contrib import admin
from .models import Clips 

# Register your models here.

@admin.register(Clips)
class ClipsAdmin(admin.ModelAdmin):
	list_display = ['id','heading']