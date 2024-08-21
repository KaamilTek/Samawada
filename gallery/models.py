from django.db import models


# Create your models here.

class Gallery(models.Model):
    
    
    image = models.ImageField(upload_to='gallery/')
    

    

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

    

