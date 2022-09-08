from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Post de Teste UnittTest", description="Blurb", wiki="Post Body test")
        self.assertEquals(post.title, "Post de Teste UnittTest")
        self.assertEquals(post.description, "Blurb")
        self.assertEquals(post.wiki, "Post Body test")
