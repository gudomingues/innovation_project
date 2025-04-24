from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name='Imagem')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    imagem = models.ImageField(upload_to='clientes/', blank=True, null=True, verbose_name='Imagem')

    def __str__(self):
        return self.nome
