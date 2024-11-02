
import django_filters
from .models import Paciente, AvalicoesSaude
from django import forms

class PacienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label="Nome",
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    genero = django_filters.ChoiceFilter(
        choices=Paciente.GENERO, 
        label="Gênero",  
        widget=forms.Select(attrs={'class': 'form-control'})
    ) 
    
    data_nascimento = django_filters.DateFromToRangeFilter(
        field_name='data_nascimento',
        label='Data de Nacimento'
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'genero']


class AvaliacaoFilter(django_filters.FilterSet):
    paciente = django_filters.ModelChoiceFilter(
        queryset=Paciente.objects.all(),
        label="Paciente",
        widget=forms.Select(attrs={'class': 'form-control'}))
    
    
    data_avalicao = django_filters.DateFromToRangeFilter(
        field_name='data_avalicao',
        label='Data da Avaliação'
    )

    sintomas = django_filters.CharFilter(lookup_expr='icontains', label="Sintomas",
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = AvalicoesSaude
        fields = ['paciente', 'sintomas' ,'data_avalicao']
