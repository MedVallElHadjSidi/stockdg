from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Depot, Envoi

from .serializers import *
# Create your views here.
@api_view(['GET', 'POST'])
def depot_list(request):

    if request.method == 'GET':
    	data = Depot.objects.all()
    	serializer = DepotSerializer(data, context={'request': request}, many=True)
    	return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def envoi_list(request):
    if request.method == 'GET':
    	data = Envoi.objects.all()
    	serializer = EnvoiSerializer(data, context={'request': request}, many=True)
    	return Response(serializer.data)
    elif request.method == 'POST':

        serializer = EnvoiSerializer(data=request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)