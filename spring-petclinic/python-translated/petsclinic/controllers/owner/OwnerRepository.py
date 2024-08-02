from django.db import models
from django.core.paginator import Paginator
from django.db.models import Q

class OwnerRepository:
    def find_pet_types(self):
        return PetType.objects.order_by('name')

    def find_by_last_name(self, last_name, page):
        owners = Owner.objects.filter(last_name__icontains=last_name)
        paginator = Paginator(owners, 5)  # 5 owners per page
        return paginator.get_page(page)

    def find_by_id(self, owner_id):
        return Owner.objects.prefetch_related('pets').get(id=owner_id)

    def save(self, owner):
        owner.save()

    def find_all(self, page):
        owners = Owner.objects.all()
        paginator = Paginator(owners, 5)  # 5 owners per page
        return paginator.get_page(page)
