from django.urls import path
from . import views



app_name = 'featured'

urlpatterns = [
    path('', views.featured_list, name='featured_list'),
    
]