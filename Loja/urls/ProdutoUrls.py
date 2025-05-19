from django.urls import path
from Loja.views.ProdutoView import list_produto_view
urlpatterns = [

    path("", list_produto_view, name='produtos'),
    path("<int:id>", list_produto_view, name='produto'),
]