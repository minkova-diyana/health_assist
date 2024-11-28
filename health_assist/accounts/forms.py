from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from health_assist.accounts.models import EmployeeProfile
from health_assist.encriptsion import encrypt_data


class EmployeeRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('uc_id_number', 'email', 'password1', 'password2')

        widgets = {
            'uc_id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'uc_id_number': 'UCN',
        }

    def clean_uc_id_number(self):

        uc_id_number = self.cleaned_data.get('uc_id_number')
        encrypted_id = encrypt_data(uc_id_number)

        if not EmployeeProfile.objects.filter(uc_id_num=encrypted_id).exists():
            raise ValidationError('The provided client number does not exist or is invalid.')

        model = get_user_model()
        if model.objects.filter(uc_id_number=encrypted_id).exists():
            raise ValidationError('The client already exists.')

        # Save the encrypted ID for later use in `save`
        self.cleaned_data['encrypted_uc_id_number'] = encrypted_id
        return uc_id_number

    def save(self, commit=True):

        user = super().save(commit=False)
        user.uc_id_number = self.cleaned_data.get('encrypted_uc_id_number')

        if commit:
            user.save()
        return user