from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#importacion de modelos.

from django.contrib.auth.models import User
class RegisterSerializers (serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('password','username','email')

    username=serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email=serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(write_only=True, required=True)
    def create(self, validate_data):
        user=User.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user