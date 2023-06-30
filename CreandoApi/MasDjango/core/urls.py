from django.urls import path
from .views import home, form_producto, form_mod_producto, form_del_producto, descargar_informe

app_name = 'informes'

urlpatterns = [
    path('', home, name="home"),
    path('form-producto', form_producto, name="form_producto"),
    path('form-mod-producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form-del-producto/<id>', form_del_producto, name="form_del_producto"),
    path('descargar-informe/', descargar_informe, name='descargar_informe'),
]