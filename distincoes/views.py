import logging
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .services import calcular_intervalos

# Configura o logger para esta view
logger = logging.getLogger(__name__)

@cache_page(60 * 15)  # Cacheia a resposta da view por 15 minutos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obter_intervalos(request):
    """
    View que retorna os intervalos entre vitórias de produtores.

    Esta view chama o serviço `calcular_intervalos` para calcular os intervalos
    entre as vitórias dos produtores e retorna o resultado em formato JSON.

    Esta view requer autenticação via token JWT.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        JsonResponse: Uma resposta JSON contendo os intervalos calculados.
    """
    logger.info('Recebida requisição para obter intervalos de vitórias de produtores')

    try:
        intervalos = calcular_intervalos()
        logger.debug('Intervalos calculados com sucesso: %s', intervalos)
        return JsonResponse(intervalos)
    except Exception as e:
        logger.error('Erro ao calcular intervalos: %s', e, exc_info=True)
        return JsonResponse({'error': 'Erro ao calcular intervalos'}, status=500)
