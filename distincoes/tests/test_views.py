import unittest
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch

class ObterIntervalosViewTestCase(APITestCase):
    """
    Testes para a view obter_intervalos, garantindo que a autenticação e a lógica
    de retorno dos intervalos de vitórias funcionem corretamente.
    """
    
    databases = {'default', 'auth_db'}  # Especifica os bancos de dados a serem usados nos testes
    
    def setUp(self):
        """
        Configuração inicial para os testes. Cria um usuário de teste e gera um token JWT para ele.
        """
        # Cria um usuário de teste com credenciais padrão
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Gera um token JWT para o usuário de teste
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        
        # Configura o cliente de teste com o token JWT no cabeçalho de autorização
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        # Define a URL da view a ser testada
        self.url = reverse('obter_intervalos')

    @patch('distincoes.views.calcular_intervalos')
    def test_obter_intervalos_authenticated(self, mock_calcular_intervalos):
        """
        Testa a view obter_intervalos para um usuário autenticado, verificando
        se a resposta contém os intervalos calculados corretamente.
        """
        # Mocka a função calcular_intervalos para retornar dados de teste
        mock_calcular_intervalos.return_value = {
            'min': [{'produtor': 'Producer 1', 'intervalo': 5, 'previousWin': 2000, 'followingWin': 2005}],
            'max': [{'produtor': 'Producer 2', 'intervalo': 10, 'previousWin': 2005, 'followingWin': 2015}]
        }

        # Faz uma requisição GET para a view
        response = self.client.get(self.url)

        # Verifica se o status code da resposta é 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o conteúdo da resposta JSON é o esperado
        self.assertEqual(response.json(), {
            'min': [{'produtor': 'Producer 1', 'intervalo': 5, 'previousWin': 2000, 'followingWin': 2005}],
            'max': [{'produtor': 'Producer 2', 'intervalo': 10, 'previousWin': 2005, 'followingWin': 2015}]
        })

    def test_obter_intervalos_unauthenticated(self):
        """
        Testa a view obter_intervalos para um usuário não autenticado,
        verificando se a resposta retorna 401 Unauthorized.
        """
        # Remove as credenciais do cliente para simular um usuário não autenticado
        self.client.credentials()  # Remove o cabeçalho de autenticação
        response = self.client.get(self.url)

        # Verifica se o status code da resposta é 401 Unauthorized
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
