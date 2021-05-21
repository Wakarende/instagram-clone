from .models import Image,Profile
from django.forms import MOdelForm


class CreateProfileForm(ModelForm):
  class Meta:
    model = Profile
    exclude = ['created', 'account_holder', 'followers', 'following']