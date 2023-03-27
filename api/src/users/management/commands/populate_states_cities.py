import requests
from django.core.management.base import BaseCommand
from users.models import State, City

#Cities and States population using Open Cage API

class Command(BaseCommand):
    help = 'Populate state and city models with data from OpenCage API'

    def handle(self, *args, **options):
        # Replace with your OpenCage API key and the country you're interested in
        api_key = 'a72fe95076914c3692548cf87c13cceb'
        country = 'Argentina'

        url = "https://api.opencagedata.com/geocode/v1/json"

        # list of states to query
        states = [
            "Buenos Aires",
            "Catamarca",
            "Chaco",
            "Chubut",
            "Córdoba",
            "Corrientes",
            "Entre Ríos",
            "Formosa",
            "Jujuy",
            "La Pampa",
            "La Rioja",
            "Mendoza",
            "Misiones",
            "Neuquén",
            "Río Negro",
            "Salta",
            "San Juan",
            "San Luis",
            "Santa Cruz",
            "Santa Fe",
            "Santiago del Estero",
            "Tierra del Fuego",
            "Tucumán"
        ]

        for state in states:
            params = {
                "key": api_key,
                "q": state + ", " + country
            }

            response = requests.get(url, params=params)
            results = response.json()["results"]

            # extract state data
            state_data = results[0]["components"]
            state_name = state_data.get("state")

            # create state object
            state_obj, created = State.objects.get_or_create(name=state_name)

            # extract cities data
            cities_data = [result["components"] for result in results[1:]]
            cities_names = [city_data.get("city") for city_data in cities_data]

            # create city objects
            for city_name in cities_names:
                if city_name is not None:
                    city_obj, created = City.objects.get_or_create(name=city_name, state=state_obj)


