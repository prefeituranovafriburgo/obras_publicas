# Generated by Django 5.0.3 on 2024-07-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscalizacao', '0001_initial'),
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
            model_name='aditivo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='fiscal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='nota_empenho',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='nota_fiscal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='nota_fiscal_arquivada',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='obra_fiscal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
