"""Vistas del módulo de reportes internos de TechNova."""

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse

from clientes.models import Cliente, Transaccion


@login_required
def reporte_clientes(request):
    """Genera un reporte interno de clientes y sus transacciones."""
    _ = request

    clientes = Cliente.objects.filter(activo=True).order_by("nombres")

    total_clientes = clientes.count()
    total_transacciones = Transaccion.objects.filter(activo=True).count()
    monto_general = (
        Transaccion.objects.filter(activo=True).aggregate(total=Sum("monto"))["total"]
        or 0
    )

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte interno de clientes - TechNova</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 30px;
                background: #f7f9fb;
                color: #222;
            }
            h1 {
                color: #1f2937;
                margin-bottom: 5px;
            }
            .subtitulo {
                color: #555;
                margin-bottom: 25px;
            }
            .resumen {
                margin-bottom: 20px;
                padding: 12px;
                background: #ffffff;
                border: 1px solid #d1d5db;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                background: #fff;
            }
            th, td {
                border: 1px solid #d1d5db;
                padding: 8px 10px;
                font-size: 14px;
            }
            th {
                background: #e5e7eb;
                text-align: left;
            }
            tr:nth-child(even) {
                background: #f9fafb;
            }
            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>Reporte interno de clientes</h1>
        <p class="subtitulo">
            Relación de clientes activos registrados en TechNova y resumen de sus transacciones.
        </p>
    """

    html += f"""
        <div class="resumen">
            <strong>Total de clientes activos:</strong> {total_clientes}<br>
            <strong>Total de transacciones activas:</strong> {total_transacciones}<br>
            <strong>Monto total procesado:</strong> S/ {monto_general}
        </div>

        <table>
            <thead>
                <tr>
                    <th>DNI</th>
                    <th>Nombres</th>
                    <th>Correo</th>
                    <th>Teléfono</th>
                    <th>Dirección</th>
                    <th>N.º transacciones</th>
                    <th>Monto total</th>
                </tr>
            </thead>
            <tbody>
    """

    for cliente in clientes:
        transacciones_cliente = Transaccion.objects.filter(
            cliente=cliente,
            activo=True,
        )

        total_transacciones_cliente = transacciones_cliente.count()
        monto_total_cliente = (
            transacciones_cliente.aggregate(total=Sum("monto"))["total"] or 0
        )

        html += f"""
            <tr>
                <td>{cliente.dni}</td>
                <td>{cliente.nombres}</td>
                <td>{cliente.correo}</td>
                <td>{cliente.telefono}</td>
                <td>{cliente.direccion}</td>
                <td>{total_transacciones_cliente}</td>
                <td>S/ {monto_total_cliente}</td>
            </tr>
        """

    html += """
            </tbody>
        </table>

        <p class="footer">
            Reporte interno generado para el sistema TechNova.
        </p>
    </body>
    </html>
    """

    return HttpResponse(html)


@login_required
def reporte_transacciones(request):
    """Genera un reporte interno de transacciones registradas."""
    _ = request

    transacciones = (
        Transaccion.objects.select_related("cliente")
        .filter(activo=True)
        .order_by("-fecha", "codigo")
    )

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte interno de transacciones - TechNova</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 30px;
                background: #f7f9fb;
                color: #222;
            }
            h1 {
                color: #1f2937;
                margin-bottom: 5px;
            }
            .subtitulo {
                color: #555;
                margin-bottom: 25px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                background: #fff;
            }
            th, td {
                border: 1px solid #d1d5db;
                padding: 8px 10px;
                font-size: 14px;
            }
            th {
                background: #e5e7eb;
                text-align: left;
            }
            tr:nth-child(even) {
                background: #f9fafb;
            }
        </style>
    </head>
    <body>
        <h1>Reporte interno de transacciones</h1>
        <p class="subtitulo">
            Relación de operaciones procesadas por TechNova.
        </p>

        <table>
            <thead>
                <tr>
                    <th>Código</th>
                    <th>Cliente</th>
                    <th>DNI</th>
                    <th>Descripción</th>
                    <th>Monto</th>
                    <th>Fecha</th>
                </tr>
            </thead>
            <tbody>
    """

    for transaccion in transacciones:
        html += f"""
            <tr>
                <td>{transaccion.codigo}</td>
                <td>{transaccion.cliente.nombres}</td>
                <td>{transaccion.cliente.dni}</td>
                <td>{transaccion.descripcion}</td>
                <td>S/ {transaccion.monto}</td>
                <td>{transaccion.fecha}</td>
            </tr>
        """

    html += """
            </tbody>
        </table>
    </body>
    </html>
    """

    return HttpResponse(html)
