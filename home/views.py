from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Appoinments 
from .serializers import AppointmentsSerializers
from django.views.generic import ListView
# Create your views here.


class AppoinmentsViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AppointmentsSerializers
    queryset = Appoinments.objects.all()



# class GeeksList(ListView):

#     # specify the model for list view
#     model = Appoinments
