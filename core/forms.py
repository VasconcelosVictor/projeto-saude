from django import forms
from .models import *

class RegisterPatientsForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'genero', 'endereco', 'telefone']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento'}),
            'genero': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Genero'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Rua, Bairro, numero'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 999999999'}),
        }

class SubmitAssessmentForm(forms.ModelForm):
    class Meta:
        model = AvalicoesSaude
        fields = ['sintomas', 'diagnostico_preliminar', 'observacoes'] 

        widgets = {
            'sintomas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: enchaqueca, nauseas'}),
            'diagnostico_preliminar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Suspeita de virose'}),
            'observacoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: a uma semana'}),
        }       
