import cloudscraper

scraper = cloudscraper.create_scraper()

def search(query:str):
    url="https://www.wollplatz.de/wolle"
    params = {'s': query}
    response = scraper.get(url, params=params)

    if response.status_code == 200:
        return response.text
    else:
        print("Request failed")
        # Some kind of error handling


def getAvailability(url:str):
    response = scraper.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print("Request failed")
        # Some kind of error handling
    