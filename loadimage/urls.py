from django.urls import re_path
 
 #importando vistas
from loadimage.views import PrimerLoadImageViewList, PrimerLoadImageViewDetail

urlpatterns=[
    re_path(r'^img/$', PrimerLoadImageViewList.as_view()),
    re_path(r'^img/(?P<pk>\d+)/$', PrimerLoadImageViewDetail.as_view()),
]