from django.urls import path, include
from petstagram.pets.views import PetCreateView, PetDeleteView, PetEditView, PetDetailView

urlpatterns = (
    path("create/", PetCreateView.as_view(), name="create pet"),

    path(
        "<str:username>/pet/<slug:pet_slug>/",
        include([
            path("", PetDetailView.as_view(), name="details pet"),
            path("edit/", PetEditView.as_view(), name="edit pet"),
            path("delete/", PetDeleteView.as_view(), name="delete pet"),
        ]),
    ),
)

"""
For FBV`s only:
"""
# from django.urls import path, include
# from petstagram.pets.views import create_pet, delete_pet, edit_pet, details_pet
#
# urlpatterns = (
#     path("create/", create_pet, name="create pet"),
#
#     path(
#         "<str:username>/pet/<slug:pet_slug>/",
#         include([
#             path("", details_pet, name="details pet"),
#             path("edit/", edit_pet, name="edit pet"),
#             path("delete/", delete_pet, name="delete pet"),
#         ]),
#     ),
# )
