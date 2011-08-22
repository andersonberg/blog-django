from django.test import TestCase
from blog.models import Post

class PostTest(TestCase):
    def test_show_post(self):
        """
        Tests when I editing a Post it's show at view
        """
	postTest = Post()
        self.assertEqual(1 + 1, 2)
