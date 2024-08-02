from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Owner, Pet, Visit
from .forms import OwnerForm, PetForm, VisitForm
from django.contrib import messages
from django.core.paginator import Paginator

class WelcomeView(View):
    def get(self, request):
        return render(request, 'welcome.html')

class OwnerView(View):
    def get(self, request, owner_id=None):
        if owner_id is None:
            form = OwnerForm()
            return render(request, 'owners/createOrUpdateOwnerForm.html', {'form': form})
        owner = get_object_or_404(Owner, id=owner_id)
        return render(request, 'owners/createOrUpdateOwnerForm.html', {'form': OwnerForm(instance=owner)})

    def post(self, request, owner_id=None):
        if owner_id is None:
            form = OwnerForm(request.POST)
            if form.is_valid():
                owner = form.save()
                messages.success(request, "New Owner Created")
                return redirect('owner_detail', owner_id=owner.id)
            else:
                messages.error(request, "There was an error in creating the owner.")
        else:
            owner = get_object_or_404(Owner, id=owner_id)
            form = OwnerForm(request.POST, instance=owner)
            if form.is_valid():
                form.save()
                messages.success(request, "Owner Values Updated")
                return redirect('owner_detail', owner_id=owner.id)
            else:
                messages.error(request, "There was an error in updating the owner.")

        return render(request, 'owners/createOrUpdateOwnerForm.html', {'form': form})

class FindOwnersView(View):    
    def get(self, request):
        last_name = request.GET.get('lastName', '')
        owners = Owner.objects.filter(last_name__icontains=last_name).order_by('last_name')
        return render(request, 'owners/findOwners.html', {'owners': owners})

class ShowOwnerView(View):   
    def get(self, request, owner_id):
        owner = get_object_or_404(Owner, id=owner_id)
        return render(request, 'owners/ownerDetails.html', {'owner': owner})
        
class FindOwnerByLastName(View):          
    def get(self, request):
        last_name = request.GET.get('lastName', '')
        owners = Owner.objects.filter(last_name__icontains=last_name).order_by('last_name')
        return render(request, 'owners/ownersList.html', {'listOwners': owners})


class PetView(View):
    def get(self, request, owner_id, pet_id=None):
        owner = get_object_or_404(Owner, id=owner_id)
        if pet_id is None:
            pet = PetForm()
            return render(request, 'pets/createOrUpdatePetForm.html', {'pet': pet, 'owner': owner})
        else:
            pet = owner.get_pet_by_id(pet_id)
            return render(request, 'pets/createOrUpdatePetForm.html', {'pet': pet, 'owner': owner})

    def post(self, request, owner_id, pet_id=None):
        owner = get_object_or_404(Owner, id=owner_id)
        if pet_id is None:
            form = PetForm(request.POST)
            if form.is_valid():
                pet = form.save(commit=False)
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
        return render(request, 'pets/createOrUpdatePetForm.html', {'pet': form, 'owner': owner})

class VisitView(View):
    def get(self, request, owner_id, pet_id):
        owner = get_object_or_404(Owner, id=owner_id)
        pet = owner.get_pet_by_id(pet_id)
        visit = Visit()
        return render(request, 'pets/createOrUpdateVisitForm.html', {'visit': visit, 'pet': pet, 'owner': owner})

    def post(self, request, owner_id, pet_id):
        owner = get_object_or_404(Owner, id=owner_id)
        pet = owner.get_pet_by_id(pet_id)
        form = VisitForm(request.POST)
        
        if form.is_valid():
            visit = form.save(commit=False)
            owner.add_visit(pet_id, visit)
            owner.save()
            messages.success(request, "Your visit has been booked")
            return redirect('owner_detail', owner_id=owner.id)
        
        return render(request, 'pets/createOrUpdateVisitForm.html', {'visit': form, 'pet': pet, 'owner': owner})

class VetsView(View):    
    def get(self, request):
        last_name = request.GET.get('lastName', '')
        owners = Owner.objects.filter(last_name__icontains=last_name).order_by('last_name')
        return render(request, 'vets/vetList.html', {'owners': owners})

class CrashView(View):
    def get(self, request):
        return render(request, 'error.html')
        #raise RuntimeError("Expected: controller used to showcase what happens when an exception is thrown")