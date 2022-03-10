from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

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

class RegisterSerializerNew(serializers.ModelSerializer):
   email = serializers.EmailField(
           required=True,
           validators=[UniqueValidator(queryset=User.objects.all())]
           )
 
   password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
   password2 = serializers.CharField(write_only=True, required=True)
 
   class Meta:
       model = User
       fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
       extra_kwargs = {
           'first_name': {'required': True},
           'last_name': {'required': True}
       }
 
   def validate(self, attrs):
       if attrs['password'] != attrs['password2']:
           raise serializers.ValidationError({"password": "Password error"})
 
       return attrs
 
   def create(self, validated_data):
       user = User.objects.create(
           username=validated_data['username'],
           email=validated_data['email'],
           first_name=validated_data['first_name'],
           last_name=validated_data['last_name']
       )
 
      
       user.set_password(validated_data['password'])
       user.save()
 
       return user