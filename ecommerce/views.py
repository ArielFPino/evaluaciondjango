from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Producto, Categoria, Marca, TipoUsuario, FormaPago, Editorial
from .forms import ClienteForm, MangaForm, EditorialForm


def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'ecommerce/lista_productos.html', context)

def ingresar_producto(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = MangaForm()
    return render(request, 'ecommerce/ingresar_producto.html', {'form': form})

def index(request):
    return render(request, 'ecommerce/index.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ecommerce/listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'ecommerce/detalle_cliente.html', {'cliente': cliente})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'ecommerce/registrar_cliente.html', {'form': form})

def guardar_manga(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = MangaForm()
    return render(request, 'ecommerce/guardar_manga.html', {'form': form})

def guardar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = EditorialForm()
    return render(request, 'ecommerce/guardar_editorial.html', {'form': form})

