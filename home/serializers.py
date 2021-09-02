from .models import *
from rest_framework import fields, serializers
from datetime import date,time
from django.contrib.auth.models import User



class AppointmentsSerializers(serializers.ModelSerializer):           
    class Meta:
        model= Appoinments
        fields = ['user', 'appoinment_date', 'appoinment_time', 'expire_time']
        

