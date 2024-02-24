from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto

from django.views import generic as views

# def index(request):
#     pet_photos = PetPhoto.objects.all()
#
#     """For search bar"""
#     pet_name_pattern = request.GET.get('pet_name_pattern', None)
#     if pet_name_pattern:
#         pet_photos = pet_photos.filter(pets__name__icontains=pet_name_pattern)
#     """End of search bar"""
#
#     context = {
#         'pet_photos': pet_photos,
#         'pet_name_pattern': pet_name_pattern,  # Adding 'pet_name_pattern' to see previous searches:
#
#     }
#     return render(request, "common/index.html", context)

""" 
Recreating 'index' view with CBV instead of FBV. 
Updating urls.py
Giving the correct template_name

Updating 'photo_list=pet_photos' to 'photo_list=object_list' to see the posts
Overwriting 'get_queryset() for search bar tool + Adding filter for our queryset
Adding @property for pet_name_pattern to use it in the code with self.pet_name_pattern
Adding paginate_by = 1, then add paginate functionality in 'index.html'
"""


class IndexView(views.ListView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related('pets') \
        .prefetch_related('photolike_set')

    template_name = "common/index.html"

    paginate_by = 1

    @property  # using property we add 'self.pet_name_pattern' only, instead of the full line
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', None)

    def get_context_data(self, *args, **kwargs):  # To see the searching word in our search bar after search initiated
        context = super().get_context_data(*args, **kwargs)
        context['pet_name_pattern'] = self.pet_name_pattern or ''
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        if pet_name_pattern:
            return queryset.filter(pets__name__icontains=pet_name_pattern)
        return queryset

    # MORE DYNAMIC:
    # def filter_by_pet_name_pattern(self, queryset):
    #     pet_name_pattern = self.request.GET.get('pet_name_pattern', None)
    #
    #     filter_query = {}
    #
    #     if pet_name_pattern:
    #         filter_query['pets__name__icontains'] = pet_name_pattern
    #     return queryset.filter(**filter_query)


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

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")

