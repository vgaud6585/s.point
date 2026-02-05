from django.shortcuts import render
from core.models import StudyRecape
# Create your views here.
def homepage(request):
	pt = "web/html/homepage.html"
	stu = StudyRecape.objects.all()
	dt = {
		'records':stu,
	}
	return render(request, pt, dt)