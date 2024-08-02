from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from .models import Pet, Owner
from .forms import PetForm

class PetView(View):
    def get(self, request, owner_id, pet_id=None):
        owner = get_object_or_404(Owner, id=owner_id)
        if pet_id is None:
            pet = Pet()
            return render(request, 'pets/createOrUpdatePetForm.html', {'pet': pet, 'owner': owner})
        else:
            pet = owner.get_pet_by_id(pet_id)
            return render(request, 'pets/createOrUpdatePetForm.html', {'pet': pet, 'owner': owner})

    def post(self, request, owner_id, pet_id=None):
        owner = get_object_or_404(Owner, id=owner_id)
        if pet_id is None:
            pet = PetForm(request.POST)
            if pet.is_valid():
                pet = pet.save(commit=False)
                owner.add_pet(pet)
                pet.save()
                messages.success(request, "New Pet has been Added")
                return redirect('owner_detail', owner_id=owner.id)
            else:
                messages.error(request, "Error adding new pet.")
        else:
            pet = owner.get_pet_by_id(pet_id)
            form = PetForm(request.POST, instance=pet)
            if form.is_valid():
                form.save()
                messages.success(request, "Pet details have been edited")
                return redirect('owner_detail', owner_id=owner.id)
            else:
                messages.error(request, "Error updating pet details.")
        return render(request, 'pets/createOrUpdatePetForm.html', {'pet': pet, 'owner': owner})
