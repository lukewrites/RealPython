from django.test import TestCase
from blog.models import Post  # this is different to the book.


class PostTest(TestCase):

    def test_str(self):
        my_title = Post(title='This is a basic title')
        self.assertEquals(str(my_title), 'This is a basic title')
        #  interesting that we still need the str(my_title) w/py3.