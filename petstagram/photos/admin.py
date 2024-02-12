from django.contrib import admin
from django.contrib.admin import ModelAdmin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(ModelAdmin):
    list_display = ('pk', 'location', 'created_at',
                    'short_description', 'tagged_pets', 'link_to_pet')

    def short_description(self, obj):
        return obj.description[:15]

    def tagged_pets(self, obj):
        return ', '.join(pet.name for pet in obj.pets.all())

    def link_to_pet(self, obj):
        return u'<a href="/">%s</a>' % obj.pk

    link_to_pet.allow_tags = True

# We can create custom things to display using functions
# 'tagged_pets' shows us the names of all tagged pets
# 'short_description' shows us the first 15 letters from the initial pet description
