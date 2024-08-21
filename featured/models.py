from django.db import models
from django.utils.text import slugify

# Create your models here.

class Featured(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    date = models.DateField()
    
    image = models.ImageField(upload_to='perfumes/')
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Featured, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'featured'
        verbose_name_plural = 'featured'

    def __str__(self) -> str:
        return self.name

