from django.urls import path
from .views import home, form_producto, form_mod_producto, form_del_producto, descargar_informe, Pag_principal, seccion_carnes, seccion_licores, seccion_snacks, seccion_verduras


urlpatterns = [
    path('', home, name="home"),
    path('form-producto', form_producto, name="form_producto"),
    path('form-mod-producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form-del-producto/<id>', form_del_producto, name="form_del_producto"),
    path('descargar-informe/', descargar_informe, name='descargar_informe'),
    path('Pag_principal/', Pag_principal, name="Pag_principal"),
    path('seccion_carnes/', seccion_carnes, name="seccion_carnes"),
    path('seccion_licores/', seccion_licores,name="seccion_licores"),
    path('seccion_snacks/', seccion_snacks, name="seccion_snacks"),
    path('seccion_verduras/', seccion_verduras, name="seccion_verduras"),
]