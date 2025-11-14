from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from Apps.principal.models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
class CategoriasView(TemplateView):
    template_name = "categorias.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['form'] = CategoriaForm()
        return context

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('principal:categoriasapp')  
        else:
            messages.error(request, 'Error al crear la categoría. Verifique los datos.')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('principal:categoriasapp') 
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'editar_categoria.html', {
        'form': form,
        'categoria': categoria,
        'categorias': Categoria.objects.all()
    })

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('principal:categoriasapp') 
    return render(request, 'eliminar_categoria.html', {
        'categorias': Categoria.objects.all()
    })

class ProductosView(TemplateView):
    template_name = "productos.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        context['form'] = ProductoForm()
        return context

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('principal:productosapp') 
        else:
            messages.error(request, 'Error al crear el producto. Verifique los datos.')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('principal:productosapp')  
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editar_producto.html', {
        'form': form,
        'producto': producto,
        'productos': Producto.objects.all()
    })

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('principal:productosapp')  
    return render(request, 'eliminar_producto.html', {
        'productos': Producto.objects.all()
    })