from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin:  # more dynamic
    user_field = "user"

    def get_object(self, queryset=None):  # This does not allow other user to edit the pet
        obj = super().get_object(queryset=queryset)
        obj_user = getattr(obj, self.user_field, None)
        if not self.request.user.is_authenticated \
                or obj_user != self.request.user:
            raise PermissionDenied
        return obj


# class OwnerRequiredMixin:
#     def get_object(self, queryset=None):  # This does not allow other user to edit the pet
#         obj = super().get_object(queryset=queryset)
#
#         if not self.request.user.is_authenticated \
#                 or obj.user != self.request.user:
#             raise PermissionDenied
#         return obj


# class OwnerRequiredMixin(auth_mixins.LoginRequiredMixin):  # adding LoginRequiredMixin to remove this: if not self.request.user.is_authenticated
#     user_field = "user"
#
#     def get_object(self, queryset=None):  # This does not allow other user to edit the pet
#         obj = super().get_object(queryset=queryset)
#         obj_user = getattr(obj, self.user_field, None)
#         if obj_user != self.request.user:
#             raise PermissionDenied
#         return obj
