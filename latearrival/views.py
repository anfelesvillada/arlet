from urllib import request
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LateArrival
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 
from latearrival.forms import LateArrivalForm

# Create your views here.
class LateArrivalListView(ListView):
    model = LateArrival
    template_name = "late_arrival_list.html"

class LateArrivalCreateView(SuccessMessageMixin, CreateView):
    model = LateArrival
    template_name = "late_arrival_new.html"
    form_class = LateArrivalForm
    #fields = ("date_arrival","observations", "document_apprentice")
    success_url = reverse_lazy('late_arrival_list')
    success_message = 'Registro de llegada tarde creado'

class LateArrivalUpdateView(UpdateView):
    model = LateArrival
    template_name =  "late_arrival_edit.html"       
    form_class = LateArrivalForm
    #fields = ['date_arrival','observations', 'document_apprentice']

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro modificado correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('late_arrival_list')

class LateArrivalDeleteView(SuccessMessageMixin, DeleteView):
    model = LateArrival  
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('late_arrival_list')



