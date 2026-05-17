from django.contrib import admin
from .models import Cliente, Transaccion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombres", "correo", "telefono", "activo")
    search_fields = ("dni", "nombres", "correo")


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("codigo", "cliente", "monto", "fecha", "activo")
    search_fields = ("codigo", "cliente__nombres", "cliente__dni")