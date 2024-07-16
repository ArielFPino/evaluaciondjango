from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/ingresar/', views.ingresar_producto, name='ingresar_producto'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('guardar_manga/', views.guardar_manga, name='guardar_manga'),
    path('guardar_editorial/', views.guardar_editorial, name='guardar_editorial'),
]
