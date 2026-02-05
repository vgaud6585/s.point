from django.shortcuts import render

# Create your views here.
def homepage(request):
	pt = "web/html/homepage.html"
	dt = {
		
	}
	return render(request, pt, dt)