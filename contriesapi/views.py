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



