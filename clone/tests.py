from django.test import TestCase

from .models import Profile, Image, Comment
from django.contrib.auth.models import User


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username="joy")
        self.profile0 = Profile(bio="Test profile", user=self.user)
        self.user.save()

        self.profile_test = Profile(
            user=self.user, profile_pic="default.jpg", bio="Test profile"
        )


    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

       
    def test_search_user(self):
        user = Profile.search_user(self.user)
        self.assertEqual(len(user), 1)


class TestComment(TestCase):
    def setUp(self):
        self.user = User(username="joy", email="joy@gmail.com", password="1234")
        self.profile = Profile(bio="Test profile", user=self.user)
        self.image = Image(
            image="default.png", name="test", caption="caption", profile=self.profile
        )
        self.comment = Comment(image=self.image, content="comment", user=self.user)

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
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        comments = Comment.objects.all()
        self.assertEqual(len(comments), 1)
        self.comment.delete_comment()
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1), 0)

    def test_get_post_comments(self):
      comments=Comment.get_post_comments(self.image)
      self.assertTrue(len(comments)>0)


class TestIMage(TestCase):
    def setUp(self):
        self.user = User(username="joy")
        self.profile = Profile(bio="Test bio", user=self.user)
        self.image = Image(
            name="test", image="defualt.png", caption="caption", profile=self.profile
        )
        image2 = Image(
            name="test2", image="image.png", caption="caption2", profile=self.profile
        )

        self.user.save()
        self.profile.save()
        self.image.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        images = Image.objects.all()
        self.assertEqual(len(images), 1)
        self.image.delete_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1), 0)

    def test_update_caption(self):
        image=Image.objects.all()
        self.image.update_caption( "new_caption")
        self.assertEqual(self.image.caption, 'new_caption')

    def test_get_profile_images(self):
        image=Image.objects.all()
        self.assertTrue(len(image)>0)
