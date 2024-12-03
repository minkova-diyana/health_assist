from django import forms

from health_assist.packages.models import ReimbursementClaims


class UploadFiles(forms.ModelForm):
    class Meta:
        model = ReimbursementClaims
        fields = ['file']