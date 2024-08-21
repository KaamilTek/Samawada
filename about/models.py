from django.db import models
from django.utils.text import slugify

# Create your models here.

class AboutUs(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(AboutUs, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self) -> str:
        return self.name

