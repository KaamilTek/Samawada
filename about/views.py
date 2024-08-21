from django.shortcuts import render

from .models import AboutUs

# Create your views here.

def about_us(request):
    about_us = AboutUs.objects.all()
    
    context = {
        'about_us': about_us,
        
        }
    return render(request, 'about/list.html', context)