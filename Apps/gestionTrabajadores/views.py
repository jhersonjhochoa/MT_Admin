from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from Apps.gestionTrabajadores.models import Trabajador
from Apps.gestionTrabajadores.forms import TrabajadorForm
from rest_framework import generics
from .models import Trabajador
from .serializers import TrabajadorSerializer
from django.shortcuts import get_object_or_404

class AddTrabajador(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'agregar_trabajadores.html'
    success_url = reverse_lazy('gestionTrabajadores:list_trabajador')

class ListTrabajador(ListView):
    queryset = Trabajador.objects.order_by('dni')
    template_name = 'listar_trabajadores.html'

class UpdateTrabajador(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'editar_trabajadores.html'
    success_url = reverse_lazy('gestionTrabajadores:list_trabajador')

class DeleteTrabajador(DeleteView):
    model = Trabajador
    template_name = 'eliminar_trabajadores.html'
    success_url = reverse_lazy('gestionTrabajadores:list_trabajador')

class viewTrabajador(generics.ListCreateAPIView):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(dni=self.request.GET.get('dni'))
