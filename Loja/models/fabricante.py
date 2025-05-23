from Loja.models import *
class Fabricante(models.Model):
    fabricante = models.CharField(null=False, max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.fabricante)