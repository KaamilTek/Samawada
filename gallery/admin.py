from django.contrib import admin

from .models import Gallery


class GalleryAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    
    list_display = ['image']
    
   

admin.site.register(Gallery ,GalleryAdmin)
