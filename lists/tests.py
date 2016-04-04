from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assetEqual(1+1,3)
