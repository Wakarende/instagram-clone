from django.test import TestCase

from .models import Profile, Image, Comment
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

class TestComment(TestCase):
  def setUp(self):
    self.user= User(username='joy', email='joy@gmail.com', password='1234')
    self.profile = Profile(bio='Test profile', user=self.user)
    self.image= Image(image='default.png', name='test', caption='caption', profile=self.profile)
    self.comment= Comment(image=self.image, content='comment', user=self.user)

    self.user.save()
    self.profile.save()
    self.image.save_image()
    self.comment.save_comment()
  
  def tearDown(self):
    Image.objects.all().delete()
    Comment.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.comment, Comment))

  def test_save_comment(self):
    comments=Comment.objects.all()
    self.assertTrue(len(comments)>0)

  def test_delete_comment(self):
    comments=Comment.objects.all()
    self.assertEqual(len(comments), 1)
    self.comment.delete_comment()
    comments1= Comment.objects.all()
    self.assertEqual(len(comments1),0)
  
  # def test_get_post_comments(self):
  #   comments=Comment.get_post_comments(self.image)
  #   self.assertEqual(comments[0].content, 'Test Comment')
  #   self.assertTrue(len(comments)>0) 

class TestIMage(TestCase):
  def setUp(self):
    self.user= User(username='joy')
    self.profile=Profile(bio='Test bio', user=self.user)
    self.image=Image(name='test' ,image='defualt.png', caption='caption',profile=self.profile)
    image2=Image(name='test2', image='image.png', caption='caption2', profile=self.profile)

    self.user.save()
    self.profile.save()
    self.image.save_image()

  def tearDown(self):
    Image.objects.all().delete()
  
  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))



