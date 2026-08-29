from django.db import models

# Create your models here.

class Transaction(models.Model):
    sender_account = models.CharField(max_length=20,blank=True)
    reciever_account = models.CharField(max_length=20,blank=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    

