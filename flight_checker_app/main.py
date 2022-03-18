# A script that uses a flight search API to locate the cheapest flights and sends text notifications when it finds a low price
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

message_sender = NotificationManager()
data = DataManager()
flight= FlightSearch()
sheety_data = data.get_request()

if sheety_data[0]["code"] =="":
    for i in sheety_data:
        i["code"] = flight.get_destination_codes(i["city"])
    data.sheety_destination = sheety_data
    data.update_sheet()
for i in sheety_data:
    flight_prices = flight.search_flight(arrival=i['code'], city=i['city'])



    if flight_prices is not None and flight_prices.price < i["lowestPrice"]:
        text = f"Lowprice alert!! pay £{flight_prices.price} to {flight_prices.destination_city}-{flight_prices.destination_airport} departing {flight_prices.origin_city}-{flight_prices.origin_airport} From {flight_prices.out_date} to {flight_prices.return_date}"

        if flight_prices.stop_overs > 0:
            text += f" Flight has {flight_prices.stop_overs} stop over, via {flight_prices.via_city}."
            print(text)

        message_sender.send_message(text)




