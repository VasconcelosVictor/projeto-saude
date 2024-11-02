from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Paciente, AvalicoesSaude

User = get_user_model()

class UserViewsTest(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login_view(self):
        """Caso de teste pra testar o Login"""
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  # Redireciona após login

    def test_logout_view(self):
        """Caso de teste pra testar o Logout"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redireciona após logout

    def test_home_view(self):
        """Caso de teste pra testar a vizualicação da tela Home"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Verifica se a página foi carregada
        self.assertTemplateUsed(response, 'home.html')  # Verifica se o template correto foi utilizado

    def test_register_patients_view(self):
        """Caso de teste pra testar o Cadastro de Paciente"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('register-patients'), {
            'nome': 'Paciente Teste',
            'data_nascimento': '2000-01-01',
            'genero': 'masculino',
            'endereco': 'Endereço Teste',
            'telefone': '123456789'
        })
        self.assertEqual(response.status_code, 302)  # Verifica redirecionamento após salvar
        self.assertEqual(Paciente.objects.count(), 1)  # Verifica se o paciente foi criado

    def test_delete_patient_view(self):
        """Caso de teste pra testar a função deletar paciente"""
        self.client.login(username='testuser', password='testpass')
        patient = Paciente.objects.create(nome='Paciente a ser excluído', data_nascimento='2000-01-01', genero='masculino', endereco='Endereço', telefone='123456789')
        response = self.client.get(reverse('delete-patient', args=[patient.id]))
        self.assertEqual(response.status_code, 302)  # Verifica redirecionamento após exclusão
        self.assertEqual(Paciente.objects.count(), 0)  # Verifica se o paciente foi excluído

    def test_assessment_list_view(self):
        """Caso de teste pra testar a visualição do historico de Avaliações"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('assessment_list'))
        self.assertEqual(response.status_code, 200)  # Verifica se a página foi carregada
        self.assertTemplateUsed(response, 'list_assessment.html')  # Verifica se o template correto foi utilizado

    def test_submit_assessment_view(self):
        """Caso de teste pra testar o cadastro de Avalições de Saude """
        self.client.login(username='testuser', password='testpass')
        patient = Paciente.objects.create(nome='Paciente para Avaliação', data_nascimento='2000-01-01', genero='masculino', endereco='Endereço', telefone='123456789')
        response = self.client.post(reverse('register-assessment', args=[patient.id]), {
            'sintomas': 'Sintoma Teste',
            'diagnostico_preliminar': 'Diagnóstico Teste',
            'observacoes': 'Observação Teste',
        })
        self.assertEqual(response.status_code, 302)  # Verifica redirecionamento após salvar
        self.assertEqual(AvalicoesSaude.objects.count(), 1)  # Verifica se a avaliação foi criada

    def test_delete_assessment_view(self):
        """Caso de teste pra testar a função Deletar Avalição de Saude"""
        self.client.login(username='testuser', password='testpass')
        patient = Paciente.objects.create(nome='Paciente para Avaliação', data_nascimento='2000-01-01', genero='masculino', endereco='Endereço', telefone='123456789')
        assessment = AvalicoesSaude.objects.create(user=self.user, paciente=patient, sintomas='Sintoma Teste')
        response = self.client.get(reverse('delete-assessment', args=[assessment.id]))
        self.assertEqual(response.status_code, 302)  # Verifica redirecionamento após exclusão
        self.assertEqual(AvalicoesSaude.objects.count(), 0)  # Verifica se a avaliação foi excluída

