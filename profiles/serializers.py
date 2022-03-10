from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import ProfilesImages

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilesImages
        fields = ('__all__')

    def create(self, img, user):
        ProfilesImages.objects.create(name_img=img,id_user=user)
    
class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','first_name','last_name','email')