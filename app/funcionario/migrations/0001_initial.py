# Generated by Django 3.0.8 on 2020-07-04 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Setor')),
                ('tipo', models.IntegerField(choices=[(1, 'Vendas Externas'), (2, 'Vendas Internas')], verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do funcionario')),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento')),
                ('cpf', models.PositiveIntegerField(verbose_name='CPF')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.Setor', verbose_name='Setor')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
