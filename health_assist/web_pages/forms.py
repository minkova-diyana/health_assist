from django import forms
from health_assist.web_pages.models import Information, Partners


class InfoBaseForm(forms.ModelForm):
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
