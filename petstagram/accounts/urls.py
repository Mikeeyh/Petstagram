from django.urls import path, include

from petstagram.accounts.views import (signup_user,
                                       signin_user,
                                       delete_profile,
                                       details_profile,
                                       edit_profile)

# from petstagram.accounts.views import *  -> This is pretty much the same. But it imports and exports at the same time.

urlpatterns = (
    path("signup/", signup_user, name="signup user"),
    path("signin/", signin_user, name="signin user"),
    path(
        "profile/<int:pk>/", include([
            path("", details_profile, name="details profile"),
            path("edit/", edit_profile, name="edit profile"),
            path("delete/", delete_profile, name="delete profile"),
        ])
    ),
)
