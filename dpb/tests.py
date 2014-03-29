from django.test import TestCase

# Create your tests here.
from dpb import models


class Test(TestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.person = models.Person.objects.create(name='Bob')
        self.bmw = models.Car.objects.create(model_name='bmw')
        self.ford = models.Car.objects.create(model_name='ford')

    def test_can_create_fave_cars(self):
        models.FaveCar(car=self.bmw, person=self.person).save()
        models.FaveCar(car=self.ford, person=self.person).save()