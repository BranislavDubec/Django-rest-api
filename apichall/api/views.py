from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from countries.models import Country
from .serializers import CountrySerializer, CountryCreateSerializer
from django.http import Http404



@api_view(['GET', 'POST'])
def handleCountries(request):
    if request.method == 'GET':
        return getCountries(request)
    elif request.method == 'POST':
        return addCountry(request)

def getCountries(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


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