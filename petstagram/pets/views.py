from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect('details pet', username='mike', pet_slug=created_pet.slug)
#
#     context = {
#         'pet_form': pet_form,
#     }
#     return render(request, 'pets/create_pet.html', context)


""" 
Recreating 'create_pet' view with CBV instead of FBV. 
Updating urls.py
Giving the correct template_name

Adding get_success_url(self) using the redirect url from FBV, but giving username and pet_slug in kwargs
"""


class PetCreateView(views.CreateView):
    # model = Pet
    # fields = ('name', 'date_of_birth', 'pet_photo')

    form_class = PetCreateForm  # No need to give 'model' and 'fields', we can only give form_class = PetCreateForm
    template_name = 'pets/create_pet.html'

    def get_success_url(self):
        return reverse('details pet', kwargs={
            "username": "mike",
            "pet_slug": self.object.slug,
        })


# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()  # To give it in our context and write 'pet_slug=pet.slug' in html
#
#     pet_form = PetEditForm(request.POST or None, instance=pet)  # 'instance=pet' to see all pet details in edit page
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             pet_form.save()
#             return redirect('details pet', username=username, pet_slug=pet_slug)
#
#     context = {
#         'pet_form': pet_form,
#
#         # we add those 2 variables too because we need them in our 'edit_pet' function
#         "username": username,
#         "pet": pet,
#     }
#     return render(request, 'pets/edit_pet.html', context)

""" 
Recreating 'edit_pet' view with CBV instead of FBV. 
Updating urls.py
Giving the correct template_name

Adding get_success_url(self) using the redirect url from FBV, but giving username and pet_slug in kwargs

Updating the edit_pet.html -> pet_from.as_p to form.as_p
Adding slug_url_kwargs because we need slug in our URL path.
Replace '<p> {{ pet.name }} </p>' with '<p> {{ object.name }} </p>' in our details_pet.html
    -> 'pet' should be replaced with 'object' everywhere.
    
Need to add model = Pet because we want to take the pet for editing
Adding get_context_data() to take our 'username'

"""


class PetEditView(views.UpdateView):
    model = Pet  # queryset = Pet.objects.all() -> Here we should add this line because we need to take the exact pet.
    form_class = PetEditForm
    template_name = 'pets/edit_pet.html'
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "mike"
        return context

    def get_success_url(self):
        return reverse('details pet', kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        })


# def details_pet(request, username, pet_slug):
#     context = {
#         'pet': Pet.objects.get(slug=pet_slug),
#     }
#     return render(request, 'pets/details_pet.html', context)

""" 
Recreating 'details_pet' view with CBV instead of FBV. 
Updating urls.py
Giving the correct template_name


Updating the details_pet.html -> pet_from.as_p to form.as_p
Adding slug_url_kwargs because we need slug in our URL path.
Replace '<p> {{ pet.name }} </p>' with '<p> {{ object.name }} </p>' in our details_pet.html
    -> 'pet' should be replaced with 'object' everywhere.
    
Need to add model = Pet because we want to take the pet for see details. 
But we take queryset using prefetch to take the Pet with its details 
(making it faster with less requests: /OPTIMISATION/)
"""


class PetDetailView(views.DetailView):
    # model = Pet  # or queryset

    queryset = Pet.objects.all()  \
        .prefetch_related("petphoto_set") \
        .prefetch_related("petphoto_set__photolike_set") \
        .prefetch_related("petphoto_set__pets")

    template_name = 'pets/details_pet.html'
    slug_url_kwarg = "pet_slug"  # name of param in URL


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         pet_form.save()
#         return redirect("index")
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#     return render(request, 'pets/delete_pet.html', context)


""" 
Recreating 'delete_pet' view with CBV instead of FBV. 
Updating urls.py
Giving the correct template_name

Adding -> success_url = reverse_lazy("index") because we do not need a dynamic here

Updating the delete_pet.html -> pet_from.as_p to form.as_p
Adding slug_url_kwargs because we need slug in our URL path.
Replace '<p> {{ pet.name }} </p>' with '<p> {{ object.name }} </p>' in our details_pet.html
    -> 'pet' should be replaced with 'object' everywhere.
    
Need to add model = Pet because we want to take the pet for deleting it
Adding 'extra_context' to take our 'username'
Adding get_form_kwargs() or get_context_data() to see the details of the pet on deleting page
"""


class PetDeleteView(views.DeleteView):
    model = Pet
    template_name = 'pets/delete_pet.html'
    form_class = PetDeleteForm

    slug_url_kwarg = "pet_slug"

    # def get_success_url(self):
    #     return reverse("index")  # static because we DO NOT need a specific URL here.

    success_url = reverse_lazy("index")

    extra_context = {
        "username": "mike",
    }

    def get_form_kwargs(self):  # TO SEE THE CONTENT ON DELETING PAGE:
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    # TO SEE THE CONTENT ON DELETING PAGE using get_context_data:

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     form = self.form_class(instance=self.object)
    #
    #     context["form"] = form
    #
    #     return context
