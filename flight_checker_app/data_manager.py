import requests
SHEETY_URL = "Your sheety URL"
SHEETY_AUTH = {"Authorization": "Your sheety auth"}
class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_get = {}

    def get_request(self):
        sheety_get = requests.get(SHEETY_URL, headers=SHEETY_AUTH).json()

        self.sheety_destination = sheety_get["prices"]

        return self.sheety_destination

    def update_sheet(self):
        for i in self.sheety_destination:
            sheety_params = {
                "price": {
                    "code":  i["code"]
                }
            }
            requests.put(f"{SHEETY_URL}/{i['id']}", headers=SHEETY_AUTH, json=sheety_params)
            print(requests.put(f"{SHEETY_URL}/{i['id']}",headers=SHEETY_AUTH).text)



