# from django.contrib import admin
# from .models import *

# admin.site.register(Status)

# admin.site.register(Nota_Fiscal)

# admin.site.register(Empresa)
# admin.site.register(Fiscal)
# admin.site.register(Fotos)
# admin.site.register(Obra)
# admin.site.register(Contrato)
# # admin.site.register(Aditivos)
# admin.site.register(Log)
# admin.site.register(Nota_Empenho)

from django.contrib import admin
from .models import (
    Status, Nota_Empenho, Nota_Fiscal, Nota_Fiscal_Arquivada, 
    Empresa, Fiscal, Obra, Contrato, Obra_Fiscal, Fotos, 
    Aditivar, Reajustar, Log
)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Nota_Empenho)
class NotaEmpenhoAdmin(admin.ModelAdmin):
    list_display = ('n_nota', 'tipo_empenho', 'data', 'valor', 'ativo', 'abatido', 'dt_inclusao')
    list_filter = ('ativo', 'abatido', 'tipo_empenho')
    search_fields = ('n_nota', 'valor')
    ordering = ('data',)

@admin.register(Nota_Fiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('n_nota', 'empenho', 'data', 'valor', 'periodo_inicial', 'periodo_final', 'ativo', 'dt_inclusao')
    list_filter = ('ativo', 'empenho')
    search_fields = ('n_nota', 'valor')
    ordering = ('periodo_inicial',)

@admin.register(Nota_Fiscal_Arquivada)
class NotaFiscalArquivadaAdmin(admin.ModelAdmin):
    list_display = ('nota', 'dt_arquivado')
    search_fields = ('nota',)
    ordering = ('dt_arquivado',)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'cadastrado_por', 'dt_inclusao')
    search_fields = ('nome', 'cnpj')
    ordering = ('nome',)

@admin.register(Fiscal)
class FiscalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crea', 'matricula', 'dt_inclusao')
    search_fields = ('nome', 'crea', 'matricula')
    ordering = ('nome',)

@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('id', 'objeto_da_obra', 'populacao_atendida', 'valor_previsto', 'status', 'fiscal', 'fiscal_substituto', 'data_inicio', 'data_conclusao', 'cadastrado_por', 'dt_inclusao')
    list_filter = ('status', 'fiscal', 'fiscal_substituto')
    search_fields = ('objeto_da_obra', 'valor_previsto')
    ordering = ('data_inicio',)

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('obra', 'empresa', 'dt_inclusao', 'user_inclusao')
    search_fields = ('obra', 'empresa')
    ordering = ('dt_inclusao',)

@admin.register(Obra_Fiscal)
class ObraFiscalAdmin(admin.ModelAdmin):
    list_display = ('obra', 'fiscal', 'status')
    list_filter = ('status', 'fiscal')
    search_fields = ('obra', 'fiscal')
    ordering = ('obra',)

@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
    list_display = ('obra', 'url')
    search_fields = ('url',)
    ordering = ('obra',)

@admin.register(Aditivar)
class AditivarAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'inicio', 'fim', 'valor', 'dt_inclusao', 'user_inclusao')
    search_fields = ('contrato', 'valor')
    ordering = ('inicio',)

@admin.register(Reajustar)
class ReajustarAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'percentual', 'valor', 'dt_inclusao', 'user_inclusao')
    search_fields = ('contrato', 'percentual', 'valor')
    ordering = ('dt_inclusao',)

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('tabela', 'ref', 'tipo', 'acao', 'dt_inclusao', 'user', 'ipv4')
    list_filter = ('tabela', 'tipo')
    search_fields = ('acao', 'user')
    ordering = ('dt_inclusao',)
