from django.db import models
from django.core.exceptions import ValidationError

class Owner(Person):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    telephone = models.CharField(max_length=10)

    pets = models.ManyToManyField('Pet', related_name='owners', blank=True)

    def clean(self):
        super().clean()
        if len(self.telephone) != 10 or not self.telephone.isdigit():
            raise ValidationError({'telephone': 'Telephone must be a 10-digit number'})

    def add_pet(self, pet):
        if pet.is_new():
            self.pets.add(pet)

    def get_pet(self, name, ignore_new=False):
        name = name.lower()
        for pet in self.pets.all():
            if pet.name.lower() == name and (ignore_new or not pet.is_new()):
                return pet
        return None

    def get_pet_by_id(self, id):
        for pet in self.pets.all():
            if not pet.is_new() and pet.id == id:
                return pet
        return None

    def __str__(self):
        return f"Owner(id={self.id}, firstName={self.first_name}, lastName={self.last_name}, address={self.address}, city={self.city}, telephone={self.telephone})"

    def add_visit(self, pet_id, visit):
        pet = self.get_pet_by_id(pet_id)
        if pet is None:
            raise ValueError("Invalid Pet identifier!")
        pet.add_visit(visit)
