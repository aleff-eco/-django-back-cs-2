from django .urls import re_path
from login.views import LoginAuth

urlpatterns = [
    re_path(r'^', LoginAuth.as_view()),
]