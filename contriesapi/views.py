from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from contriesapi.models import Contries
from contriesapi.serializers import ContriesSerializer

# Create your views here.


@api_view(['GET', 'POST'])

def countries_list(request):
    if request.method == 'GET':
        countries = Contries.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name_icontains=name)

        countries_serializer = ContriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)

    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = ContriesSerializer(data=countries_data)

        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'PUT', 'DELETE'])

def countries_detail(request, pk):
    try:
       
        countries = Contries.objects.get(pk=pk)
    except Contries.DoesNotExist:
        return JsonResponse({'message': 'The country does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        countries_serializer = ContriesSerializer(countries)
        return JsonResponse(countries_serializer.data)

    elif request.method == 'PUT':
        countries_data = JSONParser().parse(request)
        countries_serializer = ContriesSerializer(countries, data=countries_data)

        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message': 'Country was deleted Successfully!'}, status=status.HTTP_204_NO_CONTENT)






