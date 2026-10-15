from django.shortcuts import render
from models import productos

def crear(request):
    if request.method =="POST":
            productos = productos(
                nombre=request.POST["nombre"],
                descripcion=request.POST["descripcion"],
                precio=request.POST["precio"],
                stock=request.POST["stock"],
                fecha_registro=request.POST["fecha_registro"]
                )

def listar(request):
      productos = productos.objects.all()
      return render(
            request,
            "lista.html",
            {"productos": productos}
      )

def detalle(request,id):
      productos = productos.objects.get(id=id)
      return render (
            request,
            "detalle.html",
            {"productos": productos}
      )

def editar(request,id):
      productos = productos.objects.get(id=id)

      if request.method=="POST":
            productos.nombre=request.POST["nombre"],
            productos.descripcion=request.POST["descripcion"],
            productos.precio=request.POST["precio"],
            productos.stock=request.POST["stock"],
            productos.fecha_registro=request.POST["fecha_registro"]

            productos.save()

            return render(
                  request,
                  "formulario.html",
                  {"productos": productos}
            )

def eliminar(request,id):
      productos = productos.objects.get(id=id)
      productos.delete()
      return render(
            request,
            "deatlle.html",
            {"productos": productos}
      )
          