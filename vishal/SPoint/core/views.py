from django.shortcuts import render, redirect, get_object_or_404
from .models import StudyRecape
from .forms import StudyRecapForm
from django.db.models import Q

# Create your views here.
def Dashboard(request):
	if request.method == 'POST':
		form = StudyRecapForm(request.POST)
		if form.is_valid():
			# Manually saving data to the model
			StudyRecape.objects.create(heading=form.cleaned_data['heading'], description=form.cleaned_data['description'], code_snippet=form.cleaned_data['code_snippet'])
			return redirect('dashboard') # Apne dashboard ka URL name yahan likhein
	else:
		form = StudyRecapForm()
	return render(request, 'core/html/dashboard.html', {"form":form})
	
def study_recap_list(request):
	# Saara data naye se purane (latest first) order mein mangwaya
	entries = StudyRecape.objects.all().order_by('-created_at')
	return render(request, 'core/html/study_recap_list.html', {'entries': entries})


# Edit View
def edit_recap(request, pk):
    entry = get_object_or_404(StudyRecape, pk=pk)
    if request.method == "POST":
        entry.heading = request.POST.get('heading')
        entry.description = request.POST.get('description')
        entry.code_snippet = request.POST.get('code_snippet')
        entry.save()
        return redirect('dashboard')
    return render(request, 'core/html/edit_recap.html', {'entry': entry})

# Delete View
def delete_recap(request, pk):
    entry = get_object_or_404(StudyRecape, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('dashboard')
    return render(request, 'core/html/confirm_delete.html', {'entry': entry})
    
    

def study_search(request):
	query = request.GET.get('q', '')
	search_type = request.GET.get('search_type', 'all') # Dropdown se value lega
	results = []
	if query:
		lookup = Q()
		if search_type == 'heading':
			lookup = Q(heading__icontains=query)
		elif search_type == 'description':
			lookup = Q(description__icontains=query)
		elif search_type == 'code':
			lookup = Q(code_snippet__icontains=query)
		elif search_type == 'id':
			lookup = Q(id__exact=query) if query.isdigit() else Q(id__isnull=True)
		else: 
			# 'all' category ke liye
			lookup = (Q(heading__icontains=query) | Q(description__icontains=query) | Q(code_snippet__icontains=query) | (Q(id__exact=query) if query.isdigit() else Q(id__isnull=True)))
		results = StudyRecape.objects.filter(lookup).distinct()
	return render(request, 'core/html/search.html', {
        'results': results, 
        'query': query, 
        'search_type': search_type
    })



def study_detail(request, pk):
	item = get_object_or_404(StudyRecape, pk=pk)
	return render(request, 'core/html/detail.html', {'item': item})