from django.contrib import admin
from .models import Image, Comment, Profile,Follow

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)