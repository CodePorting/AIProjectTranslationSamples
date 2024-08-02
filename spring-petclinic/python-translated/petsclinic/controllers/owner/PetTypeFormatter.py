from django import forms
from .models import PetType

class PetTypeFormatter:
    def __init__(self, owners_repository):
        self.owners = owners_repository

    def print(self, pet_type):
        return pet_type.name

    def parse(self, text):
        pet_types = self.owners.find_pet_types()
        for pet_type in pet_types:
            if pet_type.name == text:
                return pet_type
        raise ValueError(f"type not found: {text}")
