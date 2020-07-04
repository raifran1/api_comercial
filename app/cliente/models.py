from django.db import models

class Endereco(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Endereço')
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    uf = models.CharField(max_length=100, verbose_name='Estado')
    latitude = models.PositiveIntegerField(verbose_name='Latitude')
    longitude = models.PositiveIntegerField(verbose_name='Longitude')

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"



class Cliente(models.Model):
    SEXO_CHOICE = [
        (1, 'Masculino'),
        (2, 'Feminino'),
        (3, 'Outro'),
    ]
    TIPO_CHOCE = [
        (1, 'Pessoa Física'),
        (2, 'Pessoa Jurídica'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome')
    sexo = models.IntegerField(choices=SEXO_CHOICE, verbose_name='Sexo')
    data_nasc = models.DateField(auto_now=False, verbose_name='Data de nascimento')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, verbose_name='Endereço')
    telefone = models.CharField(max_length=25, verbose_name='Telefone') # (86) 59888-5622
    tipo = models.IntegerField(choices=TIPO_CHOCE, verbose_name='Tipo')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


