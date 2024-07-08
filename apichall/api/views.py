from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404

from countries.models import Country
from .serializers import CountrySerializer, CountryCreateSerializer
from .pagination import CustomPagination




@api_view(['GET', 'POST'])
def handleCountries(request):
    if request.method == 'GET':
        return getCountries(request)
    elif request.method == 'POST':
        return addCountry(request)

def getCountries(request):
    country_code = request.query_params.get('country-code', None)
    if country_code:
        countries = Country.objects.filter(countryCode=country_code)
    else:
        countries = Country.objects.all()

    paginator = CustomPagination()
    paginated_countries = paginator.paginate_queryset(countries, request)
    serializer = CountrySerializer(paginated_countries, many=True)

    return  paginator.get_paginated_response(serializer.data)


def addCountry(request):
    serializer = CountryCreateSerializer(data=request.data)
    if serializer.is_valid():
        obj = CountrySerializer(serializer.save())
        return Response(obj.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def handleCountry(request, id):
    if request.method == 'GET':
        return getCountry(request, id)
    elif request.method == 'PUT':
        return updateCountry(request, id)
    

def getCountry(request, id):
    try:
        country = Country.objects.get(id=id)
    except Country.DoesNotExist:
        raise Http404("Organization was not found")
    serializer = CountrySerializer(country)
    return Response(serializer.data)

def updateCountry(request, id):
    try:
        country = Country.objects.get(id=id)
    except Country.DoesNotExist:
        raise Http404("Country was not found")
    serializer = CountryCreateSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        country.name = data.get('name', country.name)
        country.countryCode = data.get('countryCode', country.countryCode)
        if 'groupId' in data:
            country.groupId = data.get('groupId', country.groupId)
        country.save()
        updateCountry = CountrySerializer(country)
        return Response(updateCountry.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)