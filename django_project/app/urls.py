from django.urls import path
from .views import CountriesView

BASE_PATH = 'api/v1/data'

urlpatterns = [
    path(f"{BASE_PATH}/country", CountriesView.as_view(), name='countries'),
]
