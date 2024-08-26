# Generated by Django 4.2.15 on 2024-08-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscalizacao', '0002_alter_fiscal_options_alter_fotos_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aditivar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(verbose_name='Data de início/reinício')),
                ('fim', models.DateField(verbose_name='Data de término')),
                ('valor', models.CharField(max_length=20, verbose_name='Valor do aditivo(R$)')),
            ],
        ),
        migrations.DeleteModel(
            name='Aditivo',
        ),
        migrations.AlterModelOptions(
            name='nota_fiscal',
            options={'ordering': ['periodo_inicial'], 'verbose_name': 'Nota Fiscal', 'verbose_name_plural': 'Notas Fiscais'},
        ),
    ]