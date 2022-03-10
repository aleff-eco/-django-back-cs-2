from django.urls import re_path
from login.views import LoginAuth, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    re_path(r'^v1/login/', LoginAuth.as_view()),
    re_path(r'^v2/Auth2/', MyObtainTokenPairView.as_view()),
    re_path(r'^v2/refresh/', TokenRefreshView.as_view()),
]

