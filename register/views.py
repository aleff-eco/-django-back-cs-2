from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.contrib.auth.models import User
#importacion de serializadores
from register.serializers import RegisterSerializers
class RegisterView (APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request,format=None):
        serializer=RegisterSerializers(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)