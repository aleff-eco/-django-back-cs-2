from django.urls import re_path


from profiles.views import ImageUserView, ImageUserViewDetail, UserModificateViewDetail

urlpatterns = [
    re_path(r'^image/$', ImageUserView.as_view()),    
    re_path(r'^image/(?P<pk>\d+)/', ImageUserViewDetail.as_view()),
    re_path(r'^modificate/(?P<pk>\d+)/$',UserModificateViewDetail.as_view())
]