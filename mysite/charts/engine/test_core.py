from django.test import TestCase

# Create your tests here.

class AnimalTestCase(TestCase):
    def test_animals_can_speak(self):
        print ("yay")
        self.assertFalse(len("yay") == 4)