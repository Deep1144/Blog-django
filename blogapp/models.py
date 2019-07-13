from django.db import models

# Create your models here.
class blog(models.Model):
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    title = models.TextField(default="")
    subtitle = models.TextField(default="")
    sub2title = models.TextField(default="")
    content_at = models.TextField(default="")
    content_as = models.TextField(default="")
    content_as2 = models.TextField(default="")