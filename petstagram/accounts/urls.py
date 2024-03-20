from django.urls import path, include

from petstagram.accounts.views import \
    (SignInUserView,
     SignUpUserView,
     ProfileDetailsView,
     ProfileUpdateView,
     ProfileDeleteView,
     signout_user)

# from petstagram.accounts.views import *  -> This is pretty much the same. But it imports and exports at the same time.

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),
    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile"),
        ])
    ),
)
