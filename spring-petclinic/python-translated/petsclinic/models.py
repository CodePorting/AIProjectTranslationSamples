from django.utils import timezone
from django.db import models

from django.core.exceptions import ValidationError

class BaseEntity(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

    def is_new(self):
        return self.id is None
    
class NamedEntity(BaseEntity):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class PetType(NamedEntity):
    pass

class Pet(NamedEntity):
    birth_date = models.DateField()
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    visits = models.ManyToManyField('Visit', related_name='pets', blank=True)

    def add_visit(self, visit):
        visit.pet = self
        visit.save()

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def clean(self):
        if not self.first_name:
            raise ValidationError({'first_name': 'This field is required.'})
        if not self.last_name:
            raise ValidationError({'last_name': 'This field is required.'})

class Owner(Person):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    telephone = models.CharField(max_length=10)
    pets = models.ForeignKey(Pet, on_delete = models.DO_NOTHING, default=None, blank=True, null=True)

    def add_pet(self, pet):
        if pet.is_new():
            self.pets.add(pet)

    def get_pet(self, name, ignore_new=False):
        name = name.lower()
        for pet in self.pets.all():
            if pet.name.lower() == name and (ignore_new or not pet.is_new()):
                return pet
        return None
    
class Visit(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def clean(self):
        if not self.description:
            raise ValidationError('This field is required.')

    def __str__(self):
        return f"Visit(date={self.date}, description={self.description})"