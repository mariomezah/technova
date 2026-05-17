from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path


def inicio(_request):
    return HttpResponseRedirect("/admin/")


urlpatterns = [
    path("", inicio, name="inicio"),
    path("admin/", admin.site.urls),
    path("clientes/", include("clientes.urls")),
    path("reportes/", include("reportes.urls")),

]
