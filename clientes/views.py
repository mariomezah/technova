import logging
import re
from decimal import Decimal, InvalidOperation

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import DatabaseError
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from .models import Cliente, Transaccion


logger = logging.getLogger(__name__)


def validar_dni(dni):
    """
    Valida que el DNI recibido tenga un formato básico permitido.
    Para el caso ficticio TechNova se permiten entre 8 y 15 dígitos.
    """
    if not dni:
        raise ValidationError("El DNI es obligatorio.")

    dni = dni.strip()

    if not re.fullmatch(r"[0-9]{8,15}", dni):
        raise ValidationError("El DNI debe contener solo números y tener entre 8 y 15 dígitos.")

    return dni


def validar_texto(valor, campo, max_length=120):
    """
    Valida texto simple para evitar entradas vacías o demasiado extensas.
    """
    if not valor:
        raise ValidationError(f"El campo {campo} es obligatorio.")

    valor = valor.strip()

    if len(valor) > max_length:
        raise ValidationError(f"El campo {campo} no debe superar {max_length} caracteres.")

    return valor


def validar_correo(correo):
    """
    Validación básica de correo electrónico.
    """
    correo = validar_texto(correo, "correo", 120)

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
        raise ValidationError("El correo electrónico no tiene un formato válido.")

    return correo


def buscar_cliente(request):
    """
    Búsqueda segura de cliente.
    Correcciones aplicadas:
    - Valida el parámetro dni.
    - Usa ORM de Django en lugar de SQL concatenado.
    - No expone errores internos.
    """
    try:
        dni = validar_dni(request.GET.get("dni", ""))

        clientes = Cliente.objects.filter(dni=dni, activo=True)

        html = "<h1>Resultado de búsqueda segura de cliente</h1>"

        if not clientes.exists():
            html += "<p>No se encontraron clientes activos con el DNI indicado.</p>"
            return HttpResponse(html)

        for cliente in clientes:
            html += "<p>"
            html += f"ID: {cliente.id}<br>"
            html += f"DNI: {cliente.dni}<br>"
            html += f"Nombres: {cliente.nombres}<br>"
            html += f"Correo: {cliente.correo}<br>"
            html += f"Teléfono: {cliente.telefono}<br>"
            html += f"Dirección: {cliente.direccion}<br>"
            html += "</p>"

        return HttpResponse(html)

    except ValidationError as error:
        return HttpResponseBadRequest(f"Dato inválido: {error.messages[0]}")

    except DatabaseError:
        logger.exception("Error de base de datos al buscar cliente.")
        return HttpResponse("Ocurrió un error interno al procesar la búsqueda.", status=500)

    except Exception:
        logger.exception("Error inesperado al buscar cliente.")
        return HttpResponse("Ocurrió un error inesperado.", status=500)


@login_required
def registrar_cliente(request):
    """
    Registro seguro de cliente.
    Correcciones aplicadas:
    - Requiere autenticación.
    - No usa SQL concatenado.
    - Valida entradas.
    - Usa ORM de Django.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Método no permitido. Use POST.")

    try:
        dni = validar_dni(request.POST.get("dni", ""))
        nombres = validar_texto(request.POST.get("nombres", ""), "nombres", 120)
        correo = validar_correo(request.POST.get("correo", ""))
        telefono = request.POST.get("telefono", "").strip()[:20]
        direccion = request.POST.get("direccion", "").strip()[:200]

        _, creado = Cliente.objects.update_or_create(
            dni=dni,
            defaults={
                "nombres": nombres,
                "correo": correo,
                "telefono": telefono,
                "direccion": direccion,
                "activo": True,
            },
        )

        if creado:
            return HttpResponse("Cliente registrado correctamente.")

        return HttpResponse("Cliente actualizado correctamente.")

    except ValidationError as error:
        return HttpResponseBadRequest(f"Dato inválido: {error.messages[0]}")

    except DatabaseError:
        logger.exception("Error de base de datos al registrar cliente.")
        return HttpResponse("Ocurrió un error interno al registrar el cliente.", status=500)

    except Exception:
        logger.exception("Error inesperado al registrar cliente.")
        return HttpResponse("Ocurrió un error inesperado.", status=500)


@login_required
def reporte_clientes(request):
    """
    Reporte seguro de clientes.
    Correcciones aplicadas:
    - Requiere autenticación.
    - Usa ORM.
    - No construye consultas SQL manuales.
    """
    _ = request
    try:
        clientes = Cliente.objects.filter(activo=True).order_by("nombres")

        html = "<h1>Reporte seguro de clientes</h1>"
        html += "<table border='1'>"
        html += "<tr><th>ID</th><th>DNI</th><th>Nombres</th><th>Correo</th><th>Teléfono</th><th>Dirección</th></tr>"

        for cliente in clientes:
            html += "<tr>"
            html += f"<td>{cliente.id}</td>"
            html += f"<td>{cliente.dni}</td>"
            html += f"<td>{cliente.nombres}</td>"
            html += f"<td>{cliente.correo}</td>"
            html += f"<td>{cliente.telefono}</td>"
            html += f"<td>{cliente.direccion}</td>"
            html += "</tr>"

        html += "</table>"

        return HttpResponse(html)

    except DatabaseError:
        logger.exception("Error de base de datos al generar reporte de clientes.")
        return HttpResponse("Ocurrió un error interno al generar el reporte.", status=500)


@login_required
def registrar_transaccion(request):
    """
    Registro seguro de transacción.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Método no permitido. Use POST.")

    try:
        dni = validar_dni(request.POST.get("dni", ""))
        codigo = validar_texto(request.POST.get("codigo", ""), "codigo", 30)
        descripcion = validar_texto(request.POST.get("descripcion", ""), "descripcion", 200)
        monto_raw = request.POST.get("monto", "0").strip()
        fecha = request.POST.get("fecha", "").strip()

        try:
            monto = Decimal(monto_raw)
        except InvalidOperation:
            return HttpResponseBadRequest("El monto no tiene un formato válido.")

        if monto <= 0:
            return HttpResponseBadRequest("El monto debe ser mayor que cero.")

        cliente = get_object_or_404(Cliente, dni=dni, activo=True)

        Transaccion.objects.create(
            cliente=cliente,
            codigo=codigo,
            descripcion=descripcion,
            monto=monto,
            fecha=fecha,
            activo=True,
        )

        return HttpResponse("Transacción registrada correctamente.")

    except ValidationError as error:
        return HttpResponseBadRequest(f"Dato inválido: {error.messages[0]}")

    except DatabaseError:
        logger.exception("Error de base de datos al registrar transacción.")
        return HttpResponse("Ocurrió un error interno al registrar la transacción.", status=500)

    except Exception:
        logger.exception("Error inesperado al registrar transacción.")
        return HttpResponse("Ocurrió un error inesperado.", status=500)
