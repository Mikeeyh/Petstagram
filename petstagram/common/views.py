from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


def index(request):
    context = {
        'pet_photos': PetPhoto.objects.all(),
    }
    return render(request, "common/index.html", context)


def like_pet_photo(request, pk):
    # pet_photo = PetPhoto.objects.get(pk=pk, user=request.user)
    # pet_photo = PetPhoto.objects.get(pk=pk)
    # pet_photo_like = PhotoLike.objects.first(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects \
                      .filter(pet_photo_id=pk) \
                      .first()

    if pet_photo_like:
        # dislike
        pet_photo_like.delete()
    else:
        # like
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect('details photo', pk=pk)

