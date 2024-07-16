from django import forms
from .models import Cliente, Producto, Categoria, Editorial, TipoUsuario, FormaPago, Editorial

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'correo', 'tipo_usuario']

class MangaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo_barra', 'descripcion', 'precio_costo', 'precio_venta', 'editorial', 'categoria']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'estado']
