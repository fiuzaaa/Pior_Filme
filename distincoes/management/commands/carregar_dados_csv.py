import logging
from django.core.management.base import BaseCommand
from distincoes.services import carregar_dados_csv
from distincoes.models import Filme

# Configura o logger para o comando
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Carregar dados dos filmes a partir do arquivo CSV'

    def add_arguments(self, parser):
        """
        Adiciona argumentos ao comando customizado.

        Este método permite que o usuário especifique o caminho do arquivo CSV
        como um argumento opcional. Se não for especificado, um caminho padrão
        será usado.

        Args:
            parser: O objeto parser que define os argumentos do comando.
        """
        parser.add_argument(
            'filepath',
            nargs='?',
            default='data/movielist.csv',
            help='Caminho para o arquivo CSV a ser carregado (padrão: data/movielist.csv)',
        )

    def handle(self, *args, **kwargs):
        """
        Método principal do comando customizado para carregar dados dos filmes.

        Este método verifica se já existem registros na tabela Filme. Se a tabela
        não estiver vazia, uma mensagem de aviso é exibida. Caso contrário, os
        dados são carregados a partir do arquivo CSV especificado.

        Args:
            *args: Argumentos posicionais do comando.
            **kwargs: Argumentos nomeados do comando.
        """
        try:
            # Verifica se a tabela Filme já contém registros
            filme_count = Filme.objects.count()
            if filme_count > 0:
                self.stdout.write(self.style.WARNING(
                    f'Os dados já foram carregados.\nTotal: {filme_count}'
                ))
                logger.warning('Tentativa de carregar dados quando a tabela já está populada. Total de registros: %d', filme_count)
            else:
                filepath = kwargs['filepath']
                logger.info('Iniciando carregamento dos dados do arquivo: %s', filepath)
                carregar_dados_csv(filepath)
                self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso'))
                logger.info('Dados carregados com sucesso a partir do arquivo: %s', filepath)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Arquivo não encontrado: {filepath}"))
            logger.error('Arquivo não encontrado: %s', filepath)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao carregar os dados: {e}"))
            logger.error('Erro ao carregar os dados: %s', e, exc_info=True)
