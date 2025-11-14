from django.contrib import admin
from django.urls import path, include
from Apps.principal.views import (
    ProductosView, 
    CategoriasView,
    crear_producto,
    editar_producto,
    eliminar_producto,
    crear_categoria,
    editar_categoria,
    eliminar_categoria
)

app_name = 'principal'

urlpatterns = [
    path('', ProductosView.as_view(), name='principal'),
    path('productos/', ProductosView.as_view(), name='productosapp'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('categorias/', CategoriasView.as_view(), name='categoriasapp'),
    path('categorias/crear/', crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),
]