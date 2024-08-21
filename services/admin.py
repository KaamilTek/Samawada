from django.contrib import admin

from .models import Services


class ServicesAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    
    list_display = ['name' ,'content']
    search_fields = ['name', 'content' ]
   

admin.site.register(Services , ServicesAdmin)