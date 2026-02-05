from django.shortcuts import render, redirect, get_object_or_404
from .models import StudyRecape
from .forms import StudyRecapForm

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