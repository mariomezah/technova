"""Rutas del módulo de reportes internos."""

from django.urls import path

from . import views


app_name = "reportes"

urlpatterns = [
    path("clientes/", views.reporte_clientes, name="reporte_clientes"),
    path("transacciones/", views.reporte_transacciones, name="reporte_transacciones"),
]
