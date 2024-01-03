from django.shortcuts import render, get_object_or_404
from .models import Region
from django.http import HttpResponseRedirect
from django.urls import reverse


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


def listar_regiones(request):
    regiones = Region.objects.all()
    return render(request, 'listar_regiones.html', {'regiones': regiones})

def region_delete(request, idregion):
    region = get_object_or_404(Region, idregion=idregion)
    region.delete()
    return HttpResponseRedirect(reverse('listar_regiones'))


