from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    GENERO =(('masculino', 'Masculino'),
             ('feminino', 'Feminino'),
             ('outros', 'Outros'))
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(choices=GENERO, max_length=20)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    def get_assessment(self):
        return AvalicoesSaude.objects.filter(paciente=self).first()

class AvalicoesSaude(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_avalicao = models.DateField(auto_now=True)
    sintomas = models.CharField(max_length=255)
    diagnostico_preliminar = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.sintomas

