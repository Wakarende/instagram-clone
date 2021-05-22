from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path(r'',views.home,name = 'home'),
path('upload/image', views.upload_image, name = "upload_image"),
path('create_profile/',views.create_profile,name = 'create_profile'),
url(r'^profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
url(r'^like/(?P<image_id>\d+)', views.like_image, name = 'like_image'),
url(r'^comment/(?P<image_id>\d+)', views.comment,name = "comment"),
url(r'^profile/edit$', views.profile_edit,name = 'profile_edit'),
]