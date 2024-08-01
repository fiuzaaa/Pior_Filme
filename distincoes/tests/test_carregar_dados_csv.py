import unittest
from unittest.mock import patch
from distincoes.models import Filme
from distincoes.services import carregar_dados_csv

class TestCarregarDadosCSV(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="year;title;studios;producers;winner\n2022;Movie Title;Studio 1;Producer 1, Producer 2;yes\n")
    @patch('csv.reader')
    @patch('distincoes.services.Filme')
    def test_carregar_dados_csv(self, mock_filme, mock_csv_reader, mock_open):
        # Mocking CSV reader
        mock_csv_reader.return_value = iter([
            ['year', 'title', 'studios', 'producers', 'winner'],
            ['2022', 'Movie Title', 'Studio 1', 'Producer 1, Producer 2', 'yes']
        ])
        
        # Chamar a função para carregar os dados
        carregar_dados_csv('fake_path.csv')
        
        # Verificar se os registros antigos foram deletados
        mock_filme.objects.all().delete.assert_called_once()
        
        # Verificar se o método create foi chamado corretamente
        mock_filme.objects.create.assert_called_with(
            ano=2022,
            titulo='Movie Title',
            estudios='Studio 1',
            produtores='Producer 1, Producer 2',
            vencedor=True
        )

if __name__ == '__main__':
    unittest.main()
