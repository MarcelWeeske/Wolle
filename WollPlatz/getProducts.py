from api import getAvailability, search
from scraper.index import readAvailabilityFromHtml, readProductsFromHtml


def getProducts(query:str):
    searchResponse=search(query)
    productList=readProductsFromHtml(searchResponse)
    print(productList)

    for product in productList:
        availability_url = product['availabilityUrl']
        getAvailabilityResponse = getAvailability(availability_url)
        availabilityText=readAvailabilityFromHtml(getAvailabilityResponse)
        product['availability'] = availabilityText
    
    return productList
