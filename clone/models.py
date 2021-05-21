from django.db import models
from cloudinary.models import CloudinaryField
# import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  profile_pic = CloudinaryField('image')
  bio =  models.TextField(blank=True)
  followers = models.IntegerField(default=0)
  following = models.IntegerField(default=0)

  def __str__(self):
    return self.user.username

  @classmethod
  def search_user(cls,username): 
    return User.objects.filter(username = username)

class Image(models.Model):
  image = CloudinaryField("image")
  name = models.CharField(max_length=30)
  caption = models.TextField(blank=True)
  post_date = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  # likes = models.ManyToManyField(Profile, related_name="posts")

  def __str__(self):
    return self.name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

