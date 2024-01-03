from django.urls import path
from . import views
from .views import region_delete
urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('listar_regiones/', views.listar_regiones, name='listar_regiones'),
    path('crear_region/', views.crear_region, name='crear_region'),
    path('listar_empleados/', views.listar_empleados, name='listar_empleados'),
    path('region_delete<int:idregion>/', region_delete, name='region_delete'),
]
