from django.contrib import admin

from Loja.models import Fabricante
from django.contrib import admin #isso já vai estar existindo noarquivo
# Register your models here.
from .models import * #imporata nossos models

# Register your models here.
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)