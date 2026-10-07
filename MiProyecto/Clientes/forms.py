from django import forms
from .models import Lector

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['nombre_completo', 'numero_socio', 'cuota_al_dia']
        labels = {
            'nombre_completo': 'Nombre Completo',
            'numero_socio': 'Número de Socio',
            'cuota_al_dia': '¿Cuota al día?',
        }
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Maria Lopez'}),
            'numero_socio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1001'}),
            'cuota_al_dia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }