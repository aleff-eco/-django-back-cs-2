from http import server
from multiprocessing import context
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from profiles.models import ProfilesImages
from profiles.serializers import ProfilesSerializer

class FindObjects():
    def get_user(pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return 404
    def get_image(pk):
        try:
            return ProfilesImages.objects.get(id_user=pk)
        except ProfilesImages.DoesNotExist:
            return 404

class ImageUserView(APIView):
    def post(self, request, format=None):
        nameImg = request.data['name_img']
        user = FindObjects.get_user(request.data['id_user'])
        image = FindObjects.get_image(request.data['id_user'])
        if user!=404:
            if image == 404:
                serializer = ProfilesSerializer(data=request.data, context={'request':request})
                if serializer.is_valid():
                    serializer.create(nameImg,user)
                    return Response({'estatus':'Agregado correctamente'})
                else: return Response({'estatus':serializer.error_messages},status=status.HTTP_400_BAD_REQUEST)
            else: return Response({'estatus':'Este id ya está relacionado con un usuario de esta entidad'}, status=status.HTTP_400_BAD_REQUEST)
        else: return Response({'El usuario al que se le desea agregar esta imagen no existe'})
        
        
class ImageUserViewDetail(APIView):

    def get(self, request,pk,format=None):
        image = FindObjects.get_image(pk)
        if image!=404:
            serializer=ProfilesSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response('El id buscado no pertenece a la entidad', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        image = FindObjects.get_image(pk)
        
        if image!=404:
            stringImage=str(image.name_img)
            serializer = ProfilesSerializer(image)
            try:
                os.remove('assets/'+stringImage)
            except os.error:
                print('La imagen no existe en el directorio')
            image.name_img=request.data['name_img']
            image.save()
            return Response('Actualizado con éxito', status=status.HTTP_200_OK)
        else: return Response('El id requerido no existe en esta relación')


    def delete(self, request, pk, format=None):
        image = FindObjects.get_image(pk)
        if image!=404:
            serializer = ProfilesSerializer(image)
            try:
                os.remove('assets/'+str(image.name_img))
            except:
                return Response('No se ha podido eliminar la imagen por motivos externos')
            image.delete()
            return Response('Se ha eliminado correctamente', status = status.HTTP_200_OK)
        else: return Response('Id no encontrado', status=status.HTTP_400_BAD_REQUEST)

class UserModificateViewDetail(APIView):
    def customRes(self, user, status):
        response = {
            "first_name": user[0]['first_name'],
            "last_name": user[0]['last_name'],
            "username":user[0]['username'],
            "email": user[0]['email'],
            "status": status
        }
        return response

    def put(self, request, pk, format=None):

        data = request.data
        user = User.objects.filter(id = pk)
        user.update(username = data.get('username'))
        user.update(first_name = data.get('first_name'))
        user.update(last_name = data.get('last_name'))
        user.update(email = data.get('email'))
        return Response(self.customRes(user.values(),status=status.HTTP_200_OK))