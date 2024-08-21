from django.contrib import admin

from .models import AboutUs


class AboutUsAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    
    list_display = ['name' ,'content', ]
    search_fields = ['name', 'content' ]
   

admin.site.register(AboutUs , AboutUsAdmin)