from django.urls import path
from Apps.gestionTrabajadores.views import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView

app_name = 'gestionTrabajadores'
urlpatterns = [
    path('', RedirectView.as_view(url='listar', permanent=False), name='index'),
    path('ver/', viewTrabajador.as_view(), name='api_trabajador'),
    path('agregar/', login_required(AddTrabajador.as_view()), name='add_trabajador'),
    path('listar/', ListTrabajador.as_view(), name='list_trabajador'),
    path('eliminar/<pk>/', login_required(DeleteTrabajador.as_view()), name='delete_trabajador'),
    path('editar/<pk>/', login_required(UpdateTrabajador.as_view()), name='update_trabajador'),

]
