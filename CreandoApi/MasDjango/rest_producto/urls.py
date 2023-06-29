from django.urls import path
from rest_producto.views import lista_productos
from rest_producto.viewsLogin import login

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('login', login, name="login"),
]