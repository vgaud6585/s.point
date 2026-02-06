from django.shortcuts import render, redirect, get_object_or_404
from .models import Clips
from .forms import ClipsForm

# List and Add (Dono kaam ek saath)

def clip_add(request):
	if request.method == "POST":
		form = ClipsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('clip_home')
	else:
		form = ClipsForm()
	return render(request, 'ClipManager/html/clip-edit.html', {'form': form,})
	
# Clip Show 
def clip_show(request):
	clips = Clips.objects.all().order_by('-created_at')
	return render(request, 'ClipManager/html/clip-show.html', {'clips': clips,})


# Edit Clip
def clip_edit(request, pk):
    clip = get_object_or_404(Clips, pk=pk)
    if request.method == "POST":
        form = ClipsForm(request.POST, instance=clip)
        if form.is_valid():
            form.save()
            return redirect('clip_home')
    else:
        form = ClipsForm(instance=clip)
    return render(request, 'ClipManager/html/clip-edit.html', {'form':form ,})

# Delete Clip
def clip_delete(request, pk):
    clip = get_object_or_404(Clips, pk=pk)
    clip.delete()
    return redirect('clip_home')
