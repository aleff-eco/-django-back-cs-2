from distutils.command.upload import upload
from email.policy import default
from django.db import models

from django.contrib.auth.models import User

class ProfilesImages(models.Model):
    name_img = models.ImageField(blank='',default='', upload_to='img_profile')
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'img_profiles'