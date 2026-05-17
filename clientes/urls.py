from django.urls import path
from . import views


app_name = "clientes"

urlpatterns = [
    path("buscar/", views.buscar_cliente, name="buscar_cliente"),
    path("registrar/", views.registrar_cliente, name="registrar_cliente"),
    path("reporte/", views.reporte_clientes, name="reporte_clientes"),
    path("transaccion/registrar/", views.registrar_transaccion, name="registrar_transaccion"),
]
