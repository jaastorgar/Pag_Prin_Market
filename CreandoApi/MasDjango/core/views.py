from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductoForm

def home(request):
    productos = Productos.objects.all()
    datos = {
        'productos': productos
    }

    return render(request, 'core/home.html', datos)


def form_producto(request):

    datos = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_producto.html', datos)


def form_mod_producto(request, id):
    producto = Productos.objects.get(idProducto=id)

    datos = {
        'form': ProductoForm(instance=producto)
    }

    return render(request, 'core/form_mod_producto.html', datos)


def form_del_producto(request, id):
    producto = Productos.objects.get(idProducto=id)

    producto.delete()

    return redirect(to="home")