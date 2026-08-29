from rest_framework import serializers
from .models import *


class TurfSerializer(serializers.ModelSerializer):
    class Meta:
        model=Turf
        fields="__all__"

