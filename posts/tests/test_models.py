from django.test import TestCase
from posts.models import Post
from accounts.models import User


class PostTestCase(TestCase):

    def test_post(self):
        user = User.objects.create(login_id="test_login_id", nickname="boo", password="P@ssw0rd")
        Post.objects.create(user_id=user.id, content="Post: 1")
        posts = Post.objects.filter(user_id=user.id)
        self.assertEqual(posts.count(), 1)
