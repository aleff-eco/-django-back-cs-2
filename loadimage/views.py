import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

#importación de modelos
from loadimage.models import LoadImageModel

#Importación de serializadores
#importación de serializador
from loadimage.serializers import LoadImageSerializer, LoadImageSerializer2

#importación de modelo
from loadimage.models import LoadImageModel

# Create your views here.
class PrimerLoadImageViewList(APIView):

    parser_classes = [MultiPartParser, FormParser]

    
    
    def get(self, request, format=None):
        querySet=LoadImageModel.objects.all()
        serializer = LoadImageSerializer2(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        file = request.data['name_img']
        serializer = LoadImageSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            img = serializer.create(file)
            return Response({'Messages':'Success'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Messages':'Error'}, status=status.HTTP_400_BAD_REQUEST)

class PrimerLoadImageViewDetail(APIView):
    
    def get_object(self, pk):
        try:
            return LoadImageModel.objects.get(pk=pk)
        except LoadImageModel.DoesNotExist:
            return 404

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = LoadImageSerializer2(idResponse, context={'reques':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('id no encontrado', status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        file = request.data['name_img']
        if idResponse != 404:
            serializer = LoadImageSerializer(idResponse, data=request.data)
            if serializer.is_valid():
                try:
                    os.remove('assets/'+str(idResponse.name_img))
                except os.error:
                    return Response({'status':'No se puede eliminar la imagen'})
                idResponse.name_img = file
                idResponse.url_img='http://localhost:8000/assets/img/'+str(file)
                idResponse.format_img= str(file).split('.')[1]
                idResponse.save()
                return Response({'status':'realizado'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('No encontrado', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = LoadImageSerializer(idResponse, data=request.data)
            if serializer.is_valid():
                try:
                    os.remove('assets/'+str(idResponse.name_img))
                except os.error:
                    return Response({'status':'No se puede eliminar la imagen'})
                idResponse.delete()
                return Response({'status':'realizado'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Id no encontrado',status=status.HTTP_400_BAD_REQUEST)