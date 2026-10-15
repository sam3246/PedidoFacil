from django.shortcuts import render
from models import pedidos

def crear(request):
    if request.method =="POST":
        pedido = pedidos(
            num_pedido=request.POST["num_pedido"],
            cliente=request.POST["cliente"],
            fecha_pedido=request.POST["fecha_pedido"],
            descripcion_pedido=request.POST["descripcion_pedido"],
            valor=request.POST["valor"],
            estado=request.POST["estado"],
            registrador=request.POST["registrador"]
            )

def listar(request):
    pedido = pedido.objects.all()
    return render (
        request,
        "lista.html",
        {"pedido": pedido}
    )

def detalle(request, id):
    pedido = pedido.objects.get(id=id)
    return render (
        request,
        "detalle.html",
        {"pedido": pedido}
    )

def editar(request,id):
    pedido = pedido.objects.get(id=id)

    if request.method == "POST":
        pedido.num_pedido=request.POST["num_pedido"],
        pedido.cliente=request.POST["cliente"],
        pedido.fecha_pedido=request.POST["fecha_pedido"],
        pedido.descripcion_pedido=request.POST["descripcion_pedido"],
        pedido.valor=request.POST["valor"],
        pedido.estado=request.POST["estado"],
        pedido.registrador=request.POST["registrador"]

        pedido.save()

        return render(
            request,
            "formulario.html",
            {"pedido": pedido}
        )

def eliminar(request,id):
    pedido = pedido.objects.get(id=id)
    pedido.delete()
    return render(
        request,
        "detalle.html",
        {"pedido": pedido}
    )