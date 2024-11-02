from django.contrib import admin
from .models import Paciente, AvalicoesSaude

class AvalicoesSaudeInline(admin.TabularInline):
    model = AvalicoesSaude
    extra = 1  # Número de formulários em branco a serem exibidos

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'genero', 'data_criacao')
    search_fields = ('nome', 'endereco', 'telefone')  # Campos para busca
    list_filter = ('genero', 'data_nascimento')  # Filtros disponíveis no admin
    inlines = [AvalicoesSaudeInline]  # Adiciona avaliações como um inline

class AvalicoesSaudeAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data_avalicao', 'sintomas', 'diagnostico_preliminar')
    search_fields = ('paciente__nome', 'sintomas', 'diagnostico_preliminar')  # Busca por nome do paciente
    list_filter = ('data_avalicao',)  # Filtros disponíveis no admin

# Registrando os modelos com suas configurações de admin
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(AvalicoesSaude, AvalicoesSaudeAdmin)
