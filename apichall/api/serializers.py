from rest_framework import serializers
from countries.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'countryCode', 'groupId']
        extra_kwargs = {'name': {'required': True}, 'countryCode': {'required': True}}
     