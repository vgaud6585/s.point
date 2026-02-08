import os
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from .models import QuickNote, GalleryPath

def save_note(request):
    if request.method == "POST":
        text = request.POST.get('note_content')
        if text:
            QuickNote.objects.create(content=text)
    return redirect(request.META.get('HTTP_REFERER', 'gallery_home'))

def notes_list_view(request):
    notes = QuickNote.objects.all().order_by('-created_at')
    return render(request, 'notes_list.html', {'notes': notes})

##### Gallery Logic with Sub-folder Support #####

def gallery_view(request):
    # User se main path lena
    current_path = request.GET.get('folder_path', '').strip()
    
    # Path save karna sidebar ke liye
    if current_path and os.path.exists(current_path):
        GalleryPath.objects.get_or_create(path=current_path)

    saved_paths = GalleryPath.objects.all().order_by('-created_at')

    images = []
    error_message = None

    if current_path:
        if os.path.exists(current_path):
            valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
            try:
                # os.walk pure directory tree ko scan karta hai
                for root, dirs, files in os.walk(current_path):
                    for f in files:
                        if f.lower().endswith(valid_extensions):
                            # root se main folder ka gap nikalna (sub-folder path)
                            rel_dir = os.path.relpath(root, current_path)
                            
                            # Dictionary bana kar list mein daalna
                            images.append({
                                'name': f,
                                'rel_path': "" if rel_dir == "." else rel_dir
                            })
                
                if not images: 
                    error_message = "Is directory ke kisi bhi folder mein images nahi mili."
            except Exception as e: 
                error_message = f"Path access denied! Error: {str(e)}"
        else: 
            error_message = "Invalid Path! System ko ye folder nahi mila."
    
    # Pagination: Ek page par 12 images
    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {
        'page_obj': page_obj, 
        'folder_path': current_path, 
        'saved_paths': saved_paths,
        'error_message': error_message
    })

def serve_image(request):
    """
    Image ko display karne ke liye secure function.
    Ab ye 'rel' parameter bhi leta hai sub-folders ke liye.
    """
    base_path = request.GET.get('p')      # Main folder
    rel_path = request.GET.get('rel', '') # Sub-folder (optional)
    name = request.GET.get('name')       # File name
    
    # Teeno ko join karke final path banana
    full_path = os.path.join(base_path, rel_path, name)
    
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            # File extensions ke basis par sahi content_type dena (Optional Improvement)
            return HttpResponse(f.read(), content_type="image/jpeg")
    
    raise Http404
