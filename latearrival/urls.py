from django.urls import path
from .views import (LateArrivalCreateView, LateArrivalUpdateView, LateArrivalDeleteView, LateArrivalListView)

urlpatterns = [   
    path("", LateArrivalListView.as_view(), name="late_arrival_list"),
    path("latearrival/new/", LateArrivalCreateView.as_view(), name="late_arrival_new"),
    path("latearrival/<int:pk>/edit/", LateArrivalUpdateView.as_view(), name="late_arrival_edit"),
    path("latearrival/<int:pk>/delete/", LateArrivalDeleteView.as_view(), name="late_arrival_delete")
]