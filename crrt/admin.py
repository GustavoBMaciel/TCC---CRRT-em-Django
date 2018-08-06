from django.contrib import admin
from . import models

class ProdutoAdmin (admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'quantidade', 'data_criado')

# Register your models here.
admin.site.register (models.Produto, ProdutoAdmin)
admin.site.register (models.Cliente)
admin.site.register (models.Venda)