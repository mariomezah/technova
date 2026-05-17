from django.http import HttpResponse
from django.db import connection


def buscar_cliente(request):
    dni = request.GET.get("dni")

    cursor = connection.cursor()

    consulta = "SELECT id, dni, nombres, correo, telefono, direccion FROM clientes_cliente WHERE dni = '" + dni + "'"

    cursor.execute(consulta)

    filas = cursor.fetchall()

    html = "<h1>Resultado de búsqueda de cliente</h1>"

    for fila in filas:
        html += "<p>"
        html += "ID: " + str(fila[0]) + "<br>"
        html += "DNI: " + str(fila[1]) + "<br>"
        html += "Nombres: " + str(fila[2]) + "<br>"
        html += "Correo: " + str(fila[3]) + "<br>"
        html += "Teléfono: " + str(fila[4]) + "<br>"
        html += "Dirección: " + str(fila[5]) + "<br>"
        html += "</p>"

    return HttpResponse(html)


def registrar_cliente(request):
    dni = request.GET.get("dni")
    nombres = request.GET.get("nombres")
    correo = request.GET.get("correo")
    telefono = request.GET.get("telefono")
    direccion = request.GET.get("direccion")

    cursor = connection.cursor()

    consulta = (
        "INSERT INTO clientes_cliente "
        "(dni, nombres, correo, telefono, direccion, activo, fecha_registro) "
        "VALUES ('" + dni + "', '" + nombres + "', '" + correo + "', '" + telefono + "', '" + direccion + "', true, NOW())"
    )

    cursor.execute(consulta)

    return HttpResponse("Cliente registrado correctamente")


def reporte_clientes(request):
    cursor = connection.cursor()

    consulta = "SELECT id, dni, nombres, correo, telefono, direccion FROM clientes_cliente"

    cursor.execute(consulta)

    filas = cursor.fetchall()

    html = "<h1>Reporte general de clientes</h1>"
    html += "<table border='1'>"
    html += "<tr><th>ID</th><th>DNI</th><th>Nombres</th><th>Correo</th><th>Teléfono</th><th>Dirección</th></tr>"

    for fila in filas:
        html += "<tr>"
        html += "<td>" + str(fila[0]) + "</td>"
        html += "<td>" + str(fila[1]) + "</td>"
        html += "<td>" + str(fila[2]) + "</td>"
        html += "<td>" + str(fila[3]) + "</td>"
        html += "<td>" + str(fila[4]) + "</td>"
        html += "<td>" + str(fila[5]) + "</td>"
        html += "</tr>"

    html += "</table>"

    return HttpResponse(html)