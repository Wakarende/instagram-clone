from django.test import TestCase

from .models import Profile
from django.contrib.auth.models import User


# Create your tests here.
class TestProfile(TestCase):
  def setUp(self):
    self.user = User(username='joy')
    self.profile = Profile(bio='Test profile', user=self.user)
    self.user.save()

    self.profile_test= Profile(id=1, user=self.user, profile_pic='default.jpg', bio='Test profile')

  def test_instance(self):
    self.assertTrue(isinstance(self.profile_test, Profile))

  # def test_save_profile(self):
  #   self.profile_test.save_profile()
  #   new_profile = Profile.objects.all()
  #   self.assertTrue(len(after)>0)
  
  def test_search_user(self):
    user=Profile.search_user(self.user)
    self.assertEqual(len(user),1)
