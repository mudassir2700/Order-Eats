from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django.utils import timezone
import re
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save
from rest_details.models import restaurant_details


class appointManager(models.Manager):
    def appointval(self, postData,ob,ob1):
        errors = []
        # print str(datetime.today()).split()[1]-> to see just the time in datetime
        print (postData["time"])
        print (datetime.now().strftime("%H:%M"))
        if postData['date']:
            if not postData["date"] >= str(date.today()):
                errors.append("Date must be set in future!")
            if len(postData["date"]) < 1:
                errors.append("Date field can not be empty")
            print ("got to appointment post Data:", postData['date'])
        #if postData['time']:
            #if str(postData['time'])<str(datetime.now().strftime("%H:%M")):
                #if not postData["date"] >= str(date.today()):
                     #errors.append('Please enter a future time slot')
        if str(postData['time'])<str(datetime.now().strftime("%H:%M")) and str(postData["date"]) <= str(date.today()):
            errors.append('Please enter a future time slot')

        if len(Appointment.objects.filter(date = postData['date'] ,slot= postData['time'],tablename_restaur=ob.Restaurant_name)) >= ob1.no_of_reservations_per_hour:
            errors.append("Oops!! Opted Time Slot is full, Please enter different Slot")
        if len(postData['task'])<2:
            errors.append("Please insert take, must be more than 2 characters")
        #if datetime.now().strftime("%Y-%m-%d") > postData['date']:
            #errors.append("Date should not be in past")
        if len(errors)==0:
            makeappoint= Appointment.objects.create(name= str(postData['task']),date= str(postData['date']),time= postData['time'],cust_email=postData['email'],mealchoice=postData['meal_type'],tablesize=postData['persons'],slot=postData['time'],tablename_restaur=ob.Restaurant_name,tablename_slug=ob.slug,table_restaur=ob)
            return(True, makeappoint)
        else:
            return(False, errors)




class Appointment(models.Model):
    order_id= models.CharField(max_length=120, blank= True)
    s1=2
    s2=4
    s3=6
    s4=8
    s5=10

    tablesize_choices=(
    (s1,'2'),
    (s2,'4'),
    (s3,'6'),
    (s4,'8'),
    (s5,'10'),
    )

    Lunch='Lunch'
    Dinner='Dinner'

    meal_choices=(
        (Lunch,'Lunch'),
        (Dinner,'Dinner'),

        )

    t1='12:00'
    t2='13:00'
    t3='14:00'
    t4='15:00'
    t5='18:00'
    t6='19:00'
    t7='20:00'
    t8='21:00'
    t9='21:30'

    Available_slot_choices=(
        (t1,'12:00'),
        (t2,'13:00'),
        (t3,'14:00'),
        (t4,'15:00'),
        (t5,'18:00'),
        (t6,'19:00'),
        (t7,'20:00'),
        (t8,'21:00'),
        (t9,'21:30'),
        )
    order_id= models.CharField(max_length=120, blank= True)
    #user= models.ForeignKey(User, related_name="onrecord", blank=True, null=True,on_delete=models.DO_NOTHING)
    name= models.CharField(max_length=255)
    status= models.CharField(max_length=255,default='Booked')
    date= models.DateField(blank=True, null=True)
    time= models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    table_restaur = models.ForeignKey(restaurant_details,on_delete=models.SET_NULL,null=True,related_name='tablerestaurant')
    tablename_restaur=models.CharField(max_length=20,blank=False,default='Default Restaurant')
    tablename_slug=models.CharField(max_length=20,blank=False,default='Default Slug')
    contact_no=models.CharField(max_length=10,blank=False,default='1234567899')
    cust_email = models.EmailField(max_length=20,blank=False,default='Anony.chamanee@gmail.com')
    tablesize=models.PositiveIntegerField(blank=True,max_length=10,choices=tablesize_choices,default=2)
    mealchoice=models.CharField(blank=True,choices=meal_choices,default='Dinner',max_length=20)
    slot=models.CharField(blank=True,choices=Available_slot_choices,max_length=10,default='20:00')

    objects= appointManager()

    def __str__(self):
        return self.order_id

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id= unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender=Appointment)



    
        