import requests

url = "https://my-api.plantnet.org/v2/identify/all"

headers = {

}

payload = {
    "api-key": "2b10R50En4FuAtbmY1Y0dJz"
}

files = {
    "images": open("/media/tolo/New Volume/PyDeploy_Projects/Python_for_Deployment/API_FastAPI/recognize_plant_name_assignment2/assets/flower1.jpg", "rb")
}

response = requests.post(url, headers= headers, params=payload, files=files)
print(response.status_code)
print(response.text)