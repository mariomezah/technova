from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Cliente, Transaccion


@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ("dni", "nombres", "correo", "telefono", "activo", "fecha_registro")
    search_fields = ("dni", "nombres", "correo", "telefono")
    ordering = ("nombres",)
    list_per_page = 20


@admin.register(Transaccion)
class TransaccionAdmin(ModelAdmin):
    list_display = ("codigo", "cliente", "descripcion", "monto", "fecha", "activo")
    search_fields = ("codigo", "descripcion", "cliente__dni", "cliente__nombres")
    ordering = ("-fecha",)
    list_per_page = 20