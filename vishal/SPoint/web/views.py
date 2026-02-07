from django.shortcuts import render
from core.models import StudyRecape

# Create your views here.
def homepage(request):
	pt = "web/html/homepage.html"
	stu = StudyRecape.objects.all()
	dt = {
		'recaps':stu,
	}
	return render(request, pt, dt)