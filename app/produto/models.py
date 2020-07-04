from django.db import models


class Categoria(models.Model):
    TYPE_VENDA_CHOICE = [
        (1, 'Atacado'),
        (2, 'Varejo'),
    ]
    nome = models.CharField(max_length=100, verbose_name='Nome da categoria')
    tipo_venda = models.IntegerField(choices=TYPE_VENDA_CHOICE)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do produto')
    preco = models.DecimalField(verbose_name='Preço', max_digits=5, decimal_places=2) # modelo -> 10.000,50
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    estoque = models.PositiveIntegerField(verbose_name='Estoque')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'