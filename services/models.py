from django.db import models
from django.utils.text import slugify

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    
    
    icon = models.ImageField(upload_to='services/')
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Services, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self) -> str:
        return self.name

