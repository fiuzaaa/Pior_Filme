import logging
import csv
import re
from .models import Filme

# Configura o logger para este módulo
logger = logging.getLogger(__name__)

def split_producers(producers):
    """
    Divide uma string de produtores em uma lista de produtores individuais.

    A string de produtores é dividida utilizando as expressões regulares que 
    consideram as conjunções 'and' e a vírgula como delimitadores.

    Args:
        producers (str): Uma string contendo os nomes dos produtores.

    Returns:
        list: Uma lista de strings, onde cada elemento é o nome de um produtor.
    """
    logger.debug('Dividindo produtores: %s', producers)
    return [producer.strip() for producer in re.split(r',\s*and\s*|,\s*|\s*and\s*', producers)]

def carregar_dados_csv(filepath):
    """
    Carrega os dados de um arquivo CSV para o modelo Filme.

    Esta função apaga todos os registros existentes no modelo Filme antes de
    carregar novos dados a partir do CSV. Cada linha do CSV representa um filme,
    e as colunas são mapeadas para os campos do modelo Filme.

    Args:
        filepath (str): O caminho completo para o arquivo CSV.

    Returns:
        None
    """
    logger.info('Carregando dados do CSV: %s', filepath)
    try:
        # Apagar todos os registros existentes no modelo Filme
        Filme.objects.all().delete()
        logger.info('Todos os registros existentes em Filme foram deletados.')

        # Ler o CSV e carregar os dados
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # Pular a linha de cabeçalho
            for row in reader:
                try:
                    logger.debug('Processando linha: %s', row)
                    ano = int(row[0])
                    titulo = row[1]
                    estudios = row[2]
                    produtores = row[3]
                    vencedor = row[4].strip().lower() == 'yes' if row[4].strip() else False
                    
                    # Criar um novo registro no modelo Filme
                    Filme.objects.create(
                        ano=ano,
                        titulo=titulo,
                        estudios=estudios,
                        produtores=produtores,
                        vencedor=vencedor
                    )
                    logger.info('Filme criado: %s', titulo)
                except ValueError as e:
                    logger.error('Erro ao processar a linha %s: %s', row, e)
                except Exception as e:
                    logger.error('Erro geral ao processar a linha %s: %s', row, e)
    except Exception as e:
        logger.critical('Erro crítico ao carregar dados do CSV: %s', e)

def calcular_intervalos():
    """
    Calcula os intervalos de tempo entre as vitórias de produtores.

    Esta função obtém todos os filmes no banco de dados, identifica os filmes
    vencedores, e então calcula os intervalos de tempo entre vitórias consecutivas
    de cada produtor. Retorna os produtores com os menores e maiores intervalos.

    Returns:
        dict: Um dicionário com duas chaves:
            - 'min': Uma lista de dicionários com os produtores e seus menores intervalos.
            - 'max': Uma lista de dicionários com os produtores e seus maiores intervalos.
    """
    try:
        logger.info('Iniciando cálculo dos intervalos de vitórias.')
        
        # Obter todos os filmes
        todos_filmes = Filme.objects.all()
        logger.debug('Total de filmes encontrados: %d', todos_filmes.count())

        # Filtrar filmes vencedores
        vencedores = [filme for filme in todos_filmes if filme.vencedor]

        if not vencedores:
            logger.warning('Nenhum filme vencedor encontrado.')
            return {'min': [], 'max': []}

        # Dicionário para armazenar os anos dos prêmios dos produtores
        intervalos = {}

        for filme in vencedores:
            produtores = split_producers(filme.produtores)
            for produtor in produtores:
                if produtor not in intervalos:
                    intervalos[produtor] = []
                intervalos[produtor].append(filme.ano)

        # Calcular intervalos entre vitórias para cada produtor
        resultados = []
        for produtor, anos in intervalos.items():
            if len(anos) > 1:
                anos.sort()
                for i in range(len(anos) - 1):
                    intervalo = anos[i + 1] - anos[i]
                    resultados.append({
                        'produtor': produtor,
                        'intervalo': intervalo,
                        'previousWin': anos[i],
                        'followingWin': anos[i + 1]
                    })

        if resultados:
            max_intervalo = max(resultados, key=lambda x: x['intervalo'])['intervalo']
            min_intervalo = min(resultados, key=lambda x: x['intervalo'])['intervalo']

            produtores_maior_intervalo = [res for res in resultados if res['intervalo'] == max_intervalo]
            produtores_menor_intervalo = [res for res in resultados if res['intervalo'] == min_intervalo]

            logger.info('Cálculo de intervalos concluído com sucesso.')
            return {
                'min': produtores_menor_intervalo,
                'max': produtores_maior_intervalo
            }

    except Exception as e:
        logger.error('Erro ao calcular intervalos: %s', e)
        return {'min': [], 'max': []}
