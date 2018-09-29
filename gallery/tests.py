from django.test import TestCase
from .models import Picture, Location, Category
import datetime as dt


class PictureTestClass(TestCase):
    """
    class that tests the Picture class
    """

    def setUp(self):
        #setting up instance
        self.one = Picture(name = 'today')