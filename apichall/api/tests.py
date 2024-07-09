from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from countries.models import Country
from .serializers import CountrySerializer, CountryCreateSerializer

class CountryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.country1 = Country.objects.create(name='Country1', countryCode='C1')
        self.country2 = Country.objects.create(name='Country2', countryCode='C2')
        self.country3 = Country.objects.create(name='Country3', countryCode='C3')
        self.country4 = Country.objects.create(name='Country4', countryCode='C4')
        self.country5 = Country.objects.create(name='Country5', countryCode='C5')
        self.country6 = Country.objects.create(name='Country6', countryCode='C6')
        self.country7 = Country.objects.create(name='Country7', countryCode='C7')
        self.count = 7
        self.pagination = {'count': self.count, 'limit': 50, 'offset': 0}
        self.links = {'next': None, 'previous': None}

    def test_get_all_countries_payload(self):
        response = self.client.get('/countries/')
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pagination'], self.pagination)
        self.assertEqual(response.data['links'], self.links)
        self.assertEqual(response.data['results'], serializer.data)
    
    def test_get_all_countries_payload_limit(self):
        response = self.client.get('/countries/', {'limit': 5})
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        pagination = {'count': self.count, 'limit': 5, 'offset': 0}
        links = {'next': 'http://testserver/countries/?limit=5&offset=5', 'previous': None}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pagination'], pagination)
        self.assertEqual(response.data['links'], links)
    
    def test_get_all_countries_payload_limit_offset(self):
        response = self.client.get('/countries/', {'limit': 5, 'offset':1})
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        pagination = {'count': self.count, 'limit': 5, 'offset': 1}
        links = {'next': 'http://testserver/countries/?limit=5&offset=6', 'previous': 'http://testserver/countries/?limit=5'}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pagination'], pagination)
        self.assertEqual(response.data['links'], links)

    def test_get_all_countries_data(self):
        response = self.client.get('/countries/')
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_countries_with_code(self):
        response = self.client.get('/countries/', {'country-code': 'C1'})
        countries = Country.objects.filter(countryCode='C1')
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_countries_with_code_no_countries(self):
        response = self.client.get('/countries/', {'country-code': 'C8'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], [])
    
    def test_get_all_countries_limit(self):
        response = self.client.get('/countries/', {'limit': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

    def test_add_valid_country(self):
        payload_new_country =  {
            'name': 'Country10',
            'countryCode': 'C10'
        }
        response = self.client.post('/countries/', data = payload_new_country)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), self.count + 1)
    
    def test_add_invalid_country(self):
        payload_new_country =  {
            'name': '',
            'countryCode': 'C10'
        }
        response = self.client.post('/countries/', data = payload_new_country)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Country.objects.count(), self.count)
    

    def test_get_country(self):
        response = self.client.get('/countries/1')
        country = Country.objects.get(id=self.country1.id)
        serializer = CountrySerializer(country)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_get_country_invalid(self):
        response = self.client.get('/countries/10')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Organization was not found')

    
    def test_update_country(self):
        payload_update_country = {'name': 'new', 'countryCode': 'NEW', 'groupId': 10}
        response = self.client.put('/countries/1', data=payload_update_country)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        country = Country.objects.get(id=self.country1.id)
        self.assertEqual(country.name, 'new')
        self.assertEqual(country.countryCode, 'NEW')
        self.assertEqual(country.groupId, 10)

    def test_update_invalid_country(self):
        response = self.client.put('/countries/15', data={})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Country was not found')
    
    def test_update_invalid_payload(self):
        payload_update_invalid = {'name': '', 'countryCode': 'UC1'}
        response = self.client.put('/countries/1', data=payload_update_invalid)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
