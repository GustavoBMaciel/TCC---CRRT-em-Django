from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField (default=0)
    ativo = models.BooleanField (default=False)
    imagem = models.ImageField (null=True,blank=True,upload_to='galeria')
    descricao = models.TextField()
    data_criado = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.nome
        
class Cliente (models.Model):    
    cnpj = models.CharField(max_length=14)
    inscricaoestadual = models.CharField(max_length=12)
    nome = models.CharField(max_length=200)
    telefone = models.IntegerField (default=0)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField (default=0)
    bairro = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    ativo = models.BooleanField (default=False)
    email = models.EmailField()
    descricao = models.TextField(max_length=500)
    data_criado = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.nome

class Venda (models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)
    data_criado = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

