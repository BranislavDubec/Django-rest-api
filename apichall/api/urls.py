from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.handleCountries),
    path('countries/<int:id>', views.handleCountry)
]