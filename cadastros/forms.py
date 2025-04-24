from django import forms
from .models import Produto, Cliente

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'imagem']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'preco': 'Preço',
            'imagem': 'Imagem',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'imagem']
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'telefone': 'Telefone',
            'imagem': 'Imagem',
        }
