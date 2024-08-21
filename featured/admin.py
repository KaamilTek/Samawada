from django.contrib import admin

from .models import Featured


class FeaturedAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    
    list_display = ['name' ,'content', 'date']
    search_fields = ['name', 'content' ]
   

admin.site.register(Featured , FeaturedAdmin)
