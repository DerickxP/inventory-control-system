from django.contrib import admin
from .models import Produto, Movimentacao

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'categoria', 'quantidade_atual', 'estoque_minimo')
    search_fields = ('codigo', 'nome', 'categoria')
    list_filter = ('categoria',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('produto__nome',)
