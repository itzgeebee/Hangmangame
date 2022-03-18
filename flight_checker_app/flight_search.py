KIWI_URL ="https://tequila-api.kiwi.com/locations/query"
KIWI_API_KEY = "Kiwi API key"
FLIGHT_SEARCH_API = "Kiwi flight search API"
KIWI_CHEAP_FLIGHTS = "https://tequila-api.kiwi.com/v2/search"

from flight_data import FlightData
from datetime import datetime, timedelta

import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "apikey": KIWI_API_KEY
        }

        self.departure_location = "london"
        self.arrival_location = ""
        self.date_from = datetime.now().strftime("%d/%m/%Y")
        self.date_to = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        self.min_stay = 7
        self.max_stay = 28
        self.cheapest = 1
        self.trips = "round"
        self.currency = "GBP"
        self.max_stop_overs = 0


    def get_destination_codes(self, city):


        code_search_params= {
            "term":city,
        }
        destination_query = requests.get(KIWI_URL, headers=FLIGHT_SEARCH_API, params=code_search_params)

        return destination_query.json()["locations"][0]["code"]


    def search_flight(self, arrival, city):

        flight_search_params = {
            "fly_from":"LON",
            "fly_to": arrival,
            "date_from":self.date_from,
            "date_to":self.date_to,
            "nights_in_dst_from":self.min_stay,
            "nights_in_dst_to":self.max_stay,
            "flight_type":self.trips,
            "one_for_city": self.cheapest,
            "max_stopovers": self.max_stop_overs,
            "curr":self.currency
        }
        search_head ={
            "apikey":FLIGHT_SEARCH_API
        }
        try:
            flight_search = requests.get(KIWI_CHEAP_FLIGHTS, headers=search_head,
                                         params=flight_search_params).json()["data"][0]
        except IndexError:

            flight_search_params["max_stopovers"] = 1

            try:
                flight_search = requests.get(KIWI_CHEAP_FLIGHTS, headers=search_head,
                                             params=flight_search_params).json()["data"][0]
            except IndexError:
                return None
            else:
                flightdata = FlightData(
                    price=flight_search["price"],
                    origin_city=flight_search["route"][0]["cityFrom"],
                    origin_airport=flight_search["route"][0]["flyFrom"],
                    destination_city=flight_search["route"][1]["cityTo"],
                    destination_airport=flight_search["route"][1]["flyTo"],
                    out_date=flight_search["route"][0]["local_departure"].split("T")[0],
                    return_date=flight_search["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=flight_search["route"][0]["cityTo"])

                return flightdata
        else:

            flightdata = FlightData(
                price =flight_search["price"],
                origin_city=flight_search["route"][0]["cityFrom"],
                origin_airport=flight_search["route"][0]["flyFrom"],
                destination_city=flight_search["route"][0]["cityTo"],
                destination_airport=flight_search["route"][0]["flyTo"],
                out_date=flight_search["route"][0]["local_departure"].split("T")[0],
                return_date=flight_search["route"][1]["local_departure"].split("T")[0])


            print(f"Low price alert!! pay £{flightdata.price} to {flightdata.destination_city}-{flightdata.destination_airport} departing {flightdata.origin_city}-{flightdata.origin_airport} From {flightdata.out_date} to {flightdata.return_date}")

            print(f"{city}: £{flightdata.price}")
            return flightdata








