from django import forms
from .models import Owner, Pet, Visit

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'address', 'city', 'telephone']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'birth_date', 'type']

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['date', 'description']