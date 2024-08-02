from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Owner, Pet, Visit
from .forms import VisitForm

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
