from django.utils import timezone
from django.db import models
from django.db.models import DateTimeField, CharField, ManyToManyField, ForeignKey
from positions import PositionField


class AbstractModel(models.Model):

    created_at = DateTimeField(default=timezone.now(), db_index=True)


class Person(AbstractModel):

    name = CharField(max_length=50)
    fave_cars = ManyToManyField('Car', through='FaveCar')


class Car(AbstractModel):

    model_name = CharField(max_length=50)


class FaveCar(AbstractModel):

    car = ForeignKey('Car')
    person = ForeignKey('Person')

    position = PositionField(collection='person')

    class Meta(object):
        unique_together = ('car', 'person')