from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from pydantic import BaseModel, constr, ValidationError

from .external import ExternalAPIError, retrieve_country_data
from .models import Country
from .serializers import CountrySerializer


class CountryRequestModel(BaseModel):
    """
        Pydantic model to ensure the correct type of request data.
        Ensures the field 'name' is always a string.
    """
    name: constr(strict=True)


class CountriesView(APIView):
    def get(self, request):
        """Retrieve all the data from every country in the database."""
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
            Add or update data of the specified country into the database.
            If the country is already in the database, update with the latest data from the external API.
            Otherwise add the country data into the database as a new entry.
        """

        try:
            validated_request_data = CountryRequestModel(**request.data)
            country_data = retrieve_country_data(validated_request_data.name)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except ExternalAPIError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        existing_country = Country.objects.filter(iso_code=country_data['iso_code']).first()
        serializer = CountrySerializer(existing_country, data=country_data) if existing_country else CountrySerializer(data=country_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        status_code = status.HTTP_200_OK if existing_country else status.HTTP_201_CREATED
        return Response(serializer.data, status=status_code)

