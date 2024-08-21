from django.shortcuts import render
from featured.models import Featured


def home(request):

    featured = Featured.objects.all()
    featured_list = Featured.objects.all()
   
    



    context = {
        'featured' : featured ,
        'featured_list' : featured_list ,
        
        
    }

    return render(request , 'index.html' , context)