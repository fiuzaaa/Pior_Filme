from django.contrib import admin
from .models import Filme

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    """
    Customização da interface de administração do modelo Filme.
    """
    list_display = ('titulo', 'ano', 'vencedor')
    list_filter = ('ano', 'vencedor')
    search_fields = ('titulo', 'produtores', 'estudios')
    ordering = ('ano',)

