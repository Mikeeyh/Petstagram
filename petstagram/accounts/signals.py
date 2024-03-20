from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # created = False, when update
    # create = True, when create
    if not created:
        return

    # Eager save -> directly creates the profile and save it
    Profile.objects.create(user=instance)

    # Equals to: (But can run other code and do other stuff too because creating and saving is separated on two parts)
    # profile = Profile(user=instance)
    # profile.save()


"""
This means that every time on UserModel instance 'save' method is called, this script will be executed
"""
# IN APPS.PY WE SHOULD IMPORT SIGNALS IN ORDER TO CREATE THE PROFILE OF THE USER.
