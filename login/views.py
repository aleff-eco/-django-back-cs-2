# Recursos de rest-framework
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
 
class LoginAuth(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token,create=Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id':user.pk,
            'username':user.username,
            'email':user.email,
            'first_name':user.first_name,
            'last_name':user.last_name
        })
 
class MyObtainTokenPairView(TokenObtainPairView):
   permission_classes = (AllowAny,)
   serializer_class = MyTokenObtainPairSerializer