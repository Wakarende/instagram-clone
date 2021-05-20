from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class Image(models.Model):
  image = CloudinaryField("image")
  name = models.CharField(max_length=30)
  caption = models.TextField(blank=True)
  post_date = models.DateTimeField(auto_now_add=True)
  # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  # likes = models.ManyToManyField(Profile, related_name="posts")

  def __str__(self):
    return self.name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()
