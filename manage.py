#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Aumenta o limite de recursão
    sys.setrecursionlimit(1500)
    
    # Define a variável de ambiente para as configurações do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piorfilme.settings')
    
    try:
        # Importa e executa os comandos do Django a partir da linha de comando
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Fornece uma mensagem de erro clara se Django não puder ser importado
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Executa o comando passado na linha de comando
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
