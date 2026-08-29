from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *


#SECURING

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class TransactionLC(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    