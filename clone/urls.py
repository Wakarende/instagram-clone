from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path(r'',views.home,name = 'home'),
path('upload/image', views.upload_image, name = "upload_image"),
path('create_profile/',views.create_profile,name = 'create_profile'),
]