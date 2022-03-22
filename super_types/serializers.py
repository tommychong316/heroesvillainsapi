from dataclasses import fields
from rest_framework import serializers
from .models import Super_Type


class Super_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Type
        fields = ['id', 'type']