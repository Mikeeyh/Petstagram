from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views  # for CBV

from petstagram.common.models import PhotoLike
from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(views.CreateView):  # CBV
    form_class = PetPhotoCreateForm
    template_name = "photos/create_photo.html"
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })


# def create_photo(request):  # FBV
#     context = {}
#     return render(request, "photos/create_photo.html", context)


class PetPhotoDetailView(views.DetailView):  # CBV
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("pets")

    template_name = "photos/details_photo.html"


# def details_photo(request, pk):  # FBV
#     context = {
#         'pet_photo': PetPhoto.objects.get(pk=pk),
#     }
#     return render(request, "photos/details_photo.html", context)


class PetPhotoEditView(views.UpdateView):  # CBV
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")
    template_name = "photos/edit_photo.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })

# def edit_photo(request, pk):  # FBV
#     context = {}
#     return render(request, "photos/edit_photo.html", context)
