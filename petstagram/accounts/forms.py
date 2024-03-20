# from petstagram.accounts.models import PetstagramUser
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel  # PetstagramUser -> when we write the form directly in views.py we can use this.
        fields = ('email',)

    # def save(self, *args, **kwargs):
    #     self.user = super().save(*args, **kwargs)
    #     return self.user


class PetstagramChangeForm(auth_forms.UserChangeForm):  # used in admin.py
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
