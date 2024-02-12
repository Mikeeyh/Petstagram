from django import forms

from petstagram.core.form_mixins import ReadonlyFieldsFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields -> we add the variables we want to include
        # exclude -> we add the variables we do not want to include
        fields = ('name', 'date_of_birth', 'pet_photo')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'pet_photo': forms.Textarea(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            'name': 'Pet name',
            'pet_photo': 'Link to image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm, ReadonlyFieldsFormMixin):
    readonly_fields = ('date_of_birth',)

    # To make changes of this specific form only:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def clean_date_of_birth(self):
        """If 'readonly' functionality is deleted from 'inspect'
        browser menu, then DOB corrected, raises ERROR:"""
        # date_of_birth = self.cleaned_data['date_of_birth']
        # if date_of_birth != self.instance.date_of_birth:
        #     raise ValidationError("Date of birth is readonly!")\
        # return date_of_birth

        return self.instance.date_of_birth


class PetDeleteForm(PetBaseForm, ReadonlyFieldsFormMixin):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    """We overwrite the 'save' method here to be sure
    it will follow our logic and call the 'save' method from 'views'
    but the difference is that we have this logic in our form
    so our views are will be the same after deleting a pet"""
    def save(self, commit=True):
        if commit:
            # self.instance.comment.delete()
            # self.instance.likes.delete()
            self.instance.delete()
        return self.instance

