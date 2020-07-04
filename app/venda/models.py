from django.db import models

class Venda(models.Model):
    funcionario = models.ForeignKey('funcionario.Funcionario', on_delete=models.CASCADE, verbose_name='Funcionário')
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, verbose_name='Cliente')
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

class VendasProd(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, verbose_name='Venda')
    produto = models.ForeignKey('produto.Produto', on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade', null=False, default=1)

    class Meta:
        verbose_name = 'Produto da venda'
        verbose_name_plural = 'Produtos da venda'