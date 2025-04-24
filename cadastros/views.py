from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Produto, Cliente
from .forms import ProdutoForm, ClienteForm

def index(request):
    return render(request, 'cadastros/index.html')

# Produto CRUD
def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso.')
            return redirect('cadastros:index')
    else:
        form = ProdutoForm()
    return render(request, 'cadastros/produto_form.html', {'form': form, 'titulo': 'Adicionar Produto'})

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso.')
            return redirect('cadastros:index')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'cadastros/produto_form.html', {'form': form, 'titulo': 'Editar Produto'})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso.')
        return redirect('cadastros:index')
    return render(request, 'cadastros/produto_confirm_delete.html', {'produto': produto})

# Cliente CRUD
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente criado com sucesso.')
            return redirect('cadastros:index')
    else:
        form = ClienteForm()
    return render(request, 'cadastros/cliente_form.html', {'form': form, 'titulo': 'Adicionar Cliente'})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            return redirect('cadastros:index')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cadastros/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso.')
        return redirect('cadastros:index')
    return render(request, 'cadastros/cliente_confirm_delete.html', {'cliente': cliente})

# Search view
def search(request):
    query = request.GET.get('q', '')
    produtos = Produto.objects.filter(
        Q(nome__icontains=query) | Q(descricao__icontains=query)
    )
    clientes = Cliente.objects.filter(
        Q(nome__icontains=query) | Q(email__icontains=query)
    )
    return render(request, 'cadastros/search_results.html', {
        'query': query,
        'produtos': produtos,
        'clientes': clientes,
    })
