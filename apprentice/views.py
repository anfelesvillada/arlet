from django.shortcuts import render
# Instanciamos el modelo 'Apprentice' para poder usarlo en nuestras Vistas CRUD
from .models import Apprentice
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
from django.urls import reverse_lazy
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class ApprenticeListView(ListView):
    model = Apprentice  # Llamamos a la clase 'Apprentice' que se encuentra en nuestro archivo 'models.py'
    template_name = "apprentice_list.html"

class ApprenticeCreateView(SuccessMessageMixin, CreateView):
    model = Apprentice
    template_name = "apprentice_new.html"
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Apprentice' de nuestra Base de Datos 
    success_url = reverse_lazy('apprentice_list')
    success_message = 'Aprendiz creado'

class ApprenticeUpdateView(UpdateView):
    model = Apprentice
    template_name =  "apprentice_edit.html"       
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Apprentice' de nuestra Base de Datos 

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro modificado correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('apprentice_list')

class ApprenticeDeleteView(SuccessMessageMixin, DeleteView):
    model = Apprentice  
    # Redireccionamos a la página principal luego de eliminar un registro o Apprentice
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('apprentice_list')
