import requests

API_BASE_URL = 'https://restcountries.com/v3.1'


def retrieve_country_data(name: str) -> dict:
    """
    Retrieve detailed country information from the an external API.
    
    Raises:
        ExternalAPIError: If API request fails or returns invalid data.
    """

    response = requests.get(f'{API_BASE_URL}/name/{name}?fullText=true')

    if response.status_code != 200:
        raise ExternalAPIError("The requested country was not found.")

    response_data = response.json()
    if len(response_data) != 1:
        raise ExternalAPIError("The retrieved data is invalid: Invalid number of results.")
    
    country_data = response_data[0]

    try:
        return {
            "name": country_data["name"]["common"],
            "iso_code": country_data["cca3"],
            "population": country_data["population"]
        }
    except KeyError:
        raise ExternalAPIError("The retrieved data is invalid: Invalid structure of data.")


class ExternalAPIError(Exception):
    """Error fetching data from external API."""