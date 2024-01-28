import requests


def search(query:str):
    url="https://www.wollplatz.de/wolle?s=Stylecraft"
    params = {'s': query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.text
    else:
        print("Request failed")
        # Some kind of error handling


def getAvailability(url:str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print("Request failed")
        # Some kind of error handling
    