from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def crear_empleado(request):
    return render(request, 'crear_empleado.html')

def listar_empleados(request):
    return render(request, 'listar_empleados.html')

def crear_region(request):
    return render(request, 'crear_region.html')

def listar_regiones(request):
    return render(request, 'listar_regiones.html')

