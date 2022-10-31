from django.urls import path
from .views import (ApprenticeListView, ApprenticeUpdateView, ApprenticeDeleteView, ApprenticeCreateView)

urlpatterns = [   
    path("", ApprenticeListView.as_view(), name="apprentice_list"),
    path("apprentice/new/", ApprenticeCreateView.as_view(), name="apprentice_new"),
    path("apprentice/<int:pk>/edit/", ApprenticeUpdateView.as_view(), name="apprentice_edit"),
    path("apprentice/<int:pk>/delete/", ApprenticeDeleteView.as_view(), name="apprentice_delete")
]