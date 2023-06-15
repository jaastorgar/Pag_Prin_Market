from django.contrib import admin
from .models import Categoria, Productos, Cliente


admin.site.register(Categoria)
admin.site.register(Productos)
admin.site.register(Cliente)