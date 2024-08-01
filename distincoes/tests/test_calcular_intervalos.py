import unittest
from unittest.mock import patch
from distincoes.models import Filme
from distincoes.services import calcular_intervalos

class TestCalcularIntervalos(unittest.TestCase):

    @patch('distincoes.services.Filme')
    def test_calcular_intervalos(self, mock_filme):
        # Mocking Filme objects
        mock_filme.objects.all.return_value = [
            Filme(ano=2000, titulo="Movie 1", estudios="Studio 1", produtores="Producer 1", vencedor=True),
            Filme(ano=2005, titulo="Movie 2", estudios="Studio 1", produtores="Producer 1", vencedor=True),
            Filme(ano=2010, titulo="Movie 3", estudios="Studio 1", produtores="Producer 2", vencedor=True),
            Filme(ano=2015, titulo="Movie 4", estudios="Studio 1", produtores="Producer 1", vencedor=True),
        ]

        resultado = calcular_intervalos()
        
        # Verificar se o resultado tem a estrutura esperada
        self.assertIn('min', resultado)
        self.assertIn('max', resultado)

        # Verificar se os intervalos foram calculados corretamente
        self.assertEqual(len(resultado['min']), 1)
        self.assertEqual(len(resultado['max']), 1)
        self.assertEqual(resultado['min'][0]['intervalo'], 5)  # Menor intervalo entre 2000 e 2005
        self.assertEqual(resultado['max'][0]['intervalo'], 10) # Maior intervalo entre 2005 e 2015

if __name__ == '__main__':
    unittest.main()
