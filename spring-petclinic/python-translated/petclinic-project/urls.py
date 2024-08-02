


from django.urls import path
from petsclinic.views import WelcomeView, FindOwnersView, ShowOwnerView, OwnerView, FindOwnerByLastName, PetView, VetsView, VisitView, CrashView

urlpatterns = [
    path('', WelcomeView.as_view(), name='home'),
    path('owners/new/', OwnerView.as_view(), name='add_owner'),
    path('owners/find/', FindOwnersView.as_view(), name='find_owners'),
    path('owners/<int:owner_id>/edit/', OwnerView.as_view(), name='edit_owner'),
    path('owners/<int:owner_id>/', ShowOwnerView.as_view(), name='owner_detail'),
    path('owners/', FindOwnerByLastName.as_view(), name='owners_list'),
    path('owners/<int:owner_id>/pets/new/', PetView.as_view(), name='add_pet'),
    path('owners/<int:owner_id>/pets/<int:pet_id>/', PetView.as_view(), name='pet_detail'),
    path('owners/<int:owner_id>/pets/<int:pet_id>/edit/', PetView.as_view(), name='edit_pet'),
    path('owners/<int:owner_id>/pets/<int:pet_id>/visits/new/', VisitView.as_view(), name='add_visit'),
    path('vets/', VetsView.as_view(), name='vets'),
    path('oups/', CrashView.as_view(), name='error'),
]