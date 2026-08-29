from django.db import models

# Create your models here.

class Turf(models.Model):
    booking_ref = models.CharField(max_length=20,blank=True)
    customer_name = models.CharField(max_length=20,blank=True)
    payment_amt = models.FloatField()
    booked_for = models.DateTimeField(auto_now=False)
    booked_on = models.DateTimeField(auto_now=True)

    