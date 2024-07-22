from django.test import TestCase
from .models import Animal


# Create your tests here.
class AnimalTest(TestCase):
    def setUp(self):
        Animal.objects.create(name="Lion", sound="Roar")
        Animal.objects.create(name="Cat", sound="Meow")

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="Lion")
        cat = Animal.objects.get(name="Cat")

        self.assertEqual(lion.speak(), "the sound of Lion says Roar")
        self.assertEqual(cat.speak(), "the sound of Cat says Meow")

