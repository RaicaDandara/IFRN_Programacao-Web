from django.http import HttpResponse
from Loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone
def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    # produtos = Produto.objects.all()
    # produtos = Produto.objects.first()
    produtos = Produto.objects.all()
    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if produto is not None:
        produtos = produtos.filter(Produto=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)
    print(produtos)
    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    # ou se preferir
    # if id is None:
    #     id = 0
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)
    # OBS: o % indica que uma variável (nesse cado id, pq vem após o |% vai ser inserida no meio da string formatada criada)