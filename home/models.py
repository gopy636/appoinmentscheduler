from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
from datetime import *
from django.core.exceptions import ValidationError
# Create your models here.
from django.contrib.auth.models import User


def validate_appoinment_date(day):
    weekday = day.weekday()
    if weekday == 5 or weekday == 6:
        raise ValidationError(
            "appoinment not possible on weekends")

def validate_appoinment_time(x):
    H = x.strftime("%H")
    if int(H) < 9 or int(H) > 17:
        print('888888888')
        raise ValidationError(
            "appoinment is schedule in betn 9am to 5 Pm")


class Appoinments(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    appoinment_date = models.DateField(validators=[validate_appoinment_date])
    appoinment_time = models.TimeField(validators=[validate_appoinment_time])
    expire_time=models.TimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username

    # def expire_appointment(self):
    #     x = self.appoinment_time.strftime("%H:%M:%S")
    #     time_change =timedelta(hours=1)
    #     expire_time =str(x) +str(time_change)
    #     return expire_time
        
    def save(self, *args, **kwargs):
        #self.expire_time = self.appoinment_time.time() + datetime.timedelta(hours=1)
        print(type(self.appoinment_time))
        self.expire_time = datetime.time(
            self.appoinment_time.hour + 1, self.appoinment_time.minute)
        print(self.expire_time)
        super(Appoinments, self).save(*args, **kwargs)
       
       
