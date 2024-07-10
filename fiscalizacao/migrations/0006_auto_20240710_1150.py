# Generated by Django 3.2.12 on 2024-07-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscalizacao', '0005_alter_nota_empenho_n_nota'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fiscal',
            options={'verbose_name': 'Fiscal', 'verbose_name_plural': 'Fiscais'},
        ),
        migrations.AlterModelOptions(
            name='fotos',
            options={'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Situação da Obra', 'verbose_name_plural': 'Situações das Obras'},
        ),
        migrations.AddField(
            model_name='obra',
            name='n_contrato',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Número do contrato'),
        ),
        migrations.AlterField(
            model_name='nota_empenho',
            name='n_nota',
            field=models.CharField(max_length=255, unique=True, verbose_name='N. da nota de empenho'),
        ),
    ]