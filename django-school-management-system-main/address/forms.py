from django import forms
from .models import District


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

