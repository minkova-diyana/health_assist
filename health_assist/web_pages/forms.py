from django import forms
from health_assist.web_pages.models import Information, Partners
from parler.forms import TranslatableModelForm
from django.utils.translation import gettext_lazy as _

class InfoBaseForm(TranslatableModelForm):
    class Meta:
        model = Information
        exclude = ['slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'hidden_info': forms.Textarea(attrs={'class': 'form-control'}),
            'pages': forms.Select(attrs={'class': 'form-control'}),
            'type_insurance': forms.Select(attrs={'class': 'form-control'}),
        }


class InfoAddForm(InfoBaseForm):
    pass


class InfoEditForm(InfoBaseForm):
    pass


class PartnersBaseForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'


class PartnersAddForm(PartnersBaseForm):
    pass


class PartnersEditForm(PartnersBaseForm):
    pass


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label=_('Your Name'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        required=True,
        label=_('Your Email'),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    subject = forms.CharField(
        max_length=300,
        required=True,
        label=_('Subject'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    message = forms.CharField(
        required=True,
        label=_('Message'),
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
