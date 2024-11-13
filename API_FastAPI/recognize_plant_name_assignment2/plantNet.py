
import requests


class PlantNet:
    def __init__(self, PlantNet_API_KEY, imgPath):
        self.url = "https://my-api.plantnet.org/v2/identify/all"
        self.headers = {
        }

        self.payload = {
            "api_key": PlantNet_API_KEY
        }

        self.files = {
            "images": open(f'{self.file}', 'rb')
        }

        self.response = requests.post(self.url, params=self.payload, headers=self.headers, files=self.files)

    
    def get_responseStatus(self):
        return self.response.status_code
    
    def get_plantName(self):
        return self.response.json()['results'][0]['species']['commonNames'][0]

