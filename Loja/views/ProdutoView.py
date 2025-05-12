from django.http import HttpResponse
def list_produto_view(request, id=None):
    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    # ou se preferir
    # if id is None:
    #     id = 0
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)
    # OBS: o % indica que uma variável (nesse cado id, pq vem após o |% vai ser inserida no meio da string formatada criada)