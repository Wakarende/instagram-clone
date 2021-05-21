from .models import Image,Profile,Comments,Follow
from django.forms import MOdelForm


class CreateProfileForm(ModelForm):
  class Meta:
    model = Profile
    exclude = ['created', 'account_holder', 'followers', 'following']

class UploadImageForm(ModelForm):
  class Meta :
    model = Image
    exclude = ['profile', 'post_date', 'likes'] 