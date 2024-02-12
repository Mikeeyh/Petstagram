from django.contrib import admin

from petstagram.pets.models import Pet

# admin.site.register(Pet) (same but not very good)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'slug')

