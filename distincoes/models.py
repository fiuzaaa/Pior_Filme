from django.db import models

class Filme(models.Model):
    """
    Modelo que representa um filme no banco de dados.

    Attributes:
        ano (int): Ano de lançamento do filme.
        titulo (str): Título do filme.
        estudios (str): Nome do(s) estúdio(s) responsável(is) pela produção.
        produtores (str): Nome(s) do(s) produtor(es) do filme.
        vencedor (bool): Indica se o filme ganhou um prêmio (default=False).
    """
    ano = models.IntegerField()
    titulo = models.CharField(max_length=255)
    estudios = models.CharField(max_length=255)
    produtores = models.TextField()
    vencedor = models.BooleanField(default=False)

    class Meta:
        db_table = 'filmes'  # Nome da tabela no banco de dados relacional
        managed = True  # Indica se Django deve gerenciar a tabela

    def __str__(self):
        """
        Retorna uma representação em string do objeto Filme.
        
        Returns:
            str: O título do filme seguido pelo ano entre parênteses.
        """
        return f"{self.titulo} ({self.ano})"
