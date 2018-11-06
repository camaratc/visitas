# Generated by Django 2.1.2 on 2018-11-06 13:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('rg', models.CharField(max_length=15, verbose_name='RG')),
                ('foto_principal', models.ImageField(blank=True, default='cadastro/static/img/user.svg', upload_to='cadastro/static/img/upload/visitantes/principal/2018/11/06', verbose_name='Foto do Visitante')),
                ('foto_adicional', models.ImageField(blank=True, upload_to='cadastro/static/img/upload/visitantes/adicional/2018/11/06', verbose_name='Foto Adicional')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime(2018, 11, 6, 13, 30, 4, 333957), verbose_name='Data de Cadastro')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=datetime.datetime(2018, 11, 6, 13, 30, 4, 335387), verbose_name='Data')),
                ('horarioEntrada', models.TimeField(verbose_name='Horário de Entrada')),
                ('horarioSaida', models.TimeField(blank=True, null=True, verbose_name='Horário de Saída')),
                ('setor', models.CharField(max_length=100, verbose_name='Setor da Visita')),
                ('observacao', models.TextField(blank=True, max_length=1000, verbose_name='Observação')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Pessoa')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
