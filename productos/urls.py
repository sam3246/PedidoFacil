from django.urls import path
from . import views

urlspatterns = [
    path("crear/", views.crear),
    path("lista/", views.listar),
    path("detalle/", views.detalle),
    path("editar/", views.editar),
    path("eliminar/", views.eliminar)
]