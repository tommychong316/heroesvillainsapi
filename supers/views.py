from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from super_types.models import Super_Type
from .serializers import SuperSerializer
from .models import Super
from supers import serializers


@api_view(['GET', 'POST'])
def supers_list(request):
   
    if request.method == 'GET':
        
        super_type = request.query_params.get('super_type')
        print(super_type)
        queryset = Super.objects.all()
        if super_type:
            queryset = queryset.filter(super_type__type=super_type)
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)
    
        # supers = Super.objects.all()
        # serializer = SuperSerializer(supers, many=True)
        # return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
   super = get_object_or_404(Super, pk=pk)
   if request.method == 'GET':
    serializer = SuperSerializer(super)
    return Response(serializer.data)
   elif request.method == 'PUT':
       serializer = SuperSerializer(super, data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)
   elif request.method == 'DELETE':
       super.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   
# @api_view(['GET'])
# def supers_list(request):
#     super_type_param = request.query_params.get('super_type')
#     sort_param = request.query_params.get('sort')
    
#     print(super_type_param)
#     print(sort_param)

# @api_view(['GET'])
# def supers_list(request):
#     super_type_param = request.queery_params.get('super_type')
#     sort_param = request.query_params.get('sort')
#     supers = Super.objects.all()
    
#     if super_type_param:
#         supers = supers.filter(super_type__type=super_type_param)
    
#     if sort_param:
#         supers = supers.order_by(sort_param)
        
#     serializer = SuperSerializer(supers, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def super_type_list(request):
    super_types = Super_Type.objects.all()
    supers_type = {}
    for super_type in super_types:
        supers = Super.objects.filter(super_type_id=super_type.id)
        super_serializer = SuperSerializer(supers, many=True)
        supers_type[super_type.type] = {
            'type': super_type.type
        }   
    return Response(supers_type)