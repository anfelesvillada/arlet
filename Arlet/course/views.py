from django.shortcuts import render
from django.urls import reverse
from .models import Course
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

class CourseCreateView(CreateView):
    model = Course
    template_name =  "course_new.html"       
    fields = ['id','career']

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Ficha creada correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    template_name =  "course_edit.html"       
    fields = ['id','career']

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Ficha modificada correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('course_list')

class CourseDeleteView(SuccessMessageMixin, DeleteView):
    model = Course 
    #success_url = reverse_lazy("course_list")  
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Ficha eliminada correctamente.'   
        messages.success (self.request, (success_message))      
        return reverse('course_list')

