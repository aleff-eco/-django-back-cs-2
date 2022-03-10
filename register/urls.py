from django.urls import re_path

#importando vistas
from register.views import RegisterView, RegisterViewNew

urlpatterns = [
    re_path(r'^v1/register/', RegisterView.as_view()),
    re_path(r'^v2/registernew/', RegisterViewNew.as_view())
]