from django.shortcuts import render

from .models import Featured

# Create your views here.

def featured_list(request):
    featured_list = Featured.objects.all()
    
    context = {
        'featured_list': featured_list,
        
        }
    return render(request, 'featured/list.html', context)