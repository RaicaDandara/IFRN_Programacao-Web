from django.contrib import admin

from Loja.models import Fabricante
from django.contrib import admin #isso já vai estar existindo noarquivo
# Register your models here.
from .models import * #imporata nossos models
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    msgPromocao = models.CharField(null=True, max_length=100, blank=True)
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao',
    'preco', 'categoria',)
    empty_value_display = 'Vazio'
    # fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    # exclude = ('msgPromocao')
    # search_fields = ('Produto',):


# Register your models here.
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)