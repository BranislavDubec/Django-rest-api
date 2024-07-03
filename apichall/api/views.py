from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from countries.models import Country
from .serializers import CountrySerializer, CountryCreateSerializer


@api_view(['GET'])
def getData(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCountry(request):
    serializer = CountryCreateSerializer(data=request.data)
    if serializer.is_valid():
        obj = CountrySerializer(serializer.save())
        return Response(obj.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
