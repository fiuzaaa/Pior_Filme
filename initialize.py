import os
import django
from django.core.management import call_command

# Definir a variável de ambiente para o arquivo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piorfilme.settings')

# Configurar o ambiente Django
django.setup()

# Executar o comando customizado para carregar os dados a partir do CSV
call_command('carregar_dados_csv')

# Criar novas migrações para o aplicativo 'distincoes'
call_command('makemigrations', 'distincoes')

# Aplicar todas as migrações pendentes no banco de dados
call_command('migrate')
