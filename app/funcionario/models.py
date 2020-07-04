from django.db import models

class Setor(models.Model):
    TIPO_CHOICE = [
        (1, 'Vendas Externas'),
        (2, 'Vendas Internas'),
    ]
    nome = models.CharField(max_length=100, verbose_name='Nome do Setor')
    tipo = models.IntegerField(choices=TIPO_CHOICE, verbose_name="Tipo")

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores' # o django iria trazer Setors

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do funcionario')
    data_nasc = models.DateField(auto_now=False, verbose_name='Data de nascimento')
    cpf = models.PositiveIntegerField(verbose_name='CPF')
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, verbose_name='Setor')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
