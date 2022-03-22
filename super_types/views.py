from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from super_types.models import Super_Type
from .serializers import Super_TypeSerializer
from .models import Super
from super_types import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
   
    if request.method == 'GET':
        super_types = Super_Type.objects.all()
        serializer = Super_TypeSerializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Super_TypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
   super_type = get_object_or_404(Super_Type, pk=pk)
   if request.method == 'GET':
    serializer = Super_TypeSerializer(super)
    return Response(serializer.data)
   elif request.method == 'PUT':
       serializer = Super_TypeSerializer(super, data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)
   elif request.method == 'DELETE':
       super.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)