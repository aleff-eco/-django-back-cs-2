from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
# Create your models here.



class LoadImageModel(models.Model):
    
    name_img = models.ImageField(blank='', default='',upload_to='img')
    url_img = models.CharField(max_length=100, null=False)
    format_img = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    
    class Meta:
        db_table = 'loadImage'