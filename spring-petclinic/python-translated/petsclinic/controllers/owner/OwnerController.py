from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .models import Owner
from .forms import OwnerForm

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

    def find_owners(self, request):
        last_name = request.GET.get('lastName', '')
        owners = Owner.objects.filter(last_name__icontains=last_name).order_by('last_name')
        return render(request, 'owners/findOwners.html', {'owners': owners})

    def show_owner(self, request, owner_id):
        owner = get_object_or_404(Owner, id=owner_id)
        return render(request, 'owners/ownerDetails.html', {'owner': owner})
