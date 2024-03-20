from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm
from petstagram.accounts.models import Profile


# Callables:
# - all functions
# - objects with overriden '__call__' method

# class OwnerRequiredMixin(AccessMixin):  # Script took from 'LoginRequiredMixin'
#     """
#     Verify that the current user has this profile.
#     The other users cannot view other profiles.
#     Only if the user of the profile is logged in, he can see his profile.
#     """
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.pk != kwargs.get('pk', None):
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/signin_user.html"
    redirect_authenticated_user = True
    # This is to redirect to index page if user logged in but try to access login page from url


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy('index')

    # logged us automatically & redirect to index view upon registration.(func from LoginView)
    # def form_valid(self, form):
    #     """Security check complete. Log the user in."""
    #     login(self.request, form.get_user())
    #     return super().form_valid(form)

    # Same as below but we should add 'user=None' and overwrite 'save' method in our form 'PetstagramUserCreationForm'
    # def form_valid(self, form):
    #     # 'form_valid' will call 'save'
    #     result = super().form_valid(form)
    #
    #     login(self.request, form.user)
    #     return result

    # Same as below but we do not change our form. Only add 'user=None' and no overwrite of 'save'
    def form_valid(self, form):
        # 'form_valid' will call 'save'
        result = super().form_valid(form)

        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):  # Add "OwnerRequiredMixin" if needed
    queryset = Profile.objects \
        .prefetch_related('user') \
        .all()

    # we add prefetch_related in order to show the user's email on profile details page without accessing the DB again

    template_name = "accounts/details_profile.html"


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    # OR USING FORM: (just remove get_form method and add get_object method if needed)
    # model = UserModel
    # form_class = ProfileEditForm
    # template_name = "accounts/edit_profile.html"

    def get_success_url(self):
        return reverse("details profile", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["date_of_birth"].widget.attrs["type"] = "date"

        return form


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete_profile.html"
