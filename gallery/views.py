from django.shortcuts import render

from .models import Gallery

# Create your views here.

def gallery_store(request):
    gallery_store = Gallery.objects.all()
    
    context = {
        'gallery_store': gallery_store,
        
        }
    return render(request, 'gallery/galleries.html', context)