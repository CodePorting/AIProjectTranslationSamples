from django.db import models
from django.utils import timezone

class Pet(NamedEntity):
    birth_date = models.DateField()
    type = models.ForeignKey('PetType', on_delete=models.CASCADE)
    visits = models.ManyToManyField('Visit', related_name='pets', blank=True)

    def add_visit(self, visit):
        visit.pet = self
        visit.save()
