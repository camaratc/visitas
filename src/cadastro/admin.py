from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Pessoa
from .models import Visita

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf', 'rg', 'endereco', 'bairro', 'estado', 'cidade', 'data_cadastro')
    list_filter = ('estado', 'cidade', ('data_cadastro', DateRangeFilter))
    list_display = ('nome', 'cpf', 'rg', 'endereco','bairro', 'estado', 'cidade', 'data_cadastro')
    ordering = ['nome']

class VisitaAdmin(admin.ModelAdmin):
    search_fields = ('pessoa', 'setor', 'data', 'horarioEntrada', 'horarioSaida')
    list_filter = ('setor', ('data', DateRangeFilter))
    list_display = ('pessoa', 'setor', 'data', 'horarioEntrada', 'horarioSaida')
    ordering = ['-pk']

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Visita, VisitaAdmin)
