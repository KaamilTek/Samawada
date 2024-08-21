from django.shortcuts import render

from .models import Services

# Create your views here.

def service_list(request):
    service_list = Services.objects.all()
    
    context = {
        'service_list': service_list,
        
        }
    return render(request, 'services/list.html', context)