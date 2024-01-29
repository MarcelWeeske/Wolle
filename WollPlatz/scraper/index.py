from bs4 import BeautifulSoup

def readProductsFromHtml(htmlContent):
    productList=[]

    soup = BeautifulSoup(htmlContent, 'html.parser')
    productDivs = soup.find_all('div', class_='productlist25')

    for productDiv in productDivs:
        innerProductDiv = productDiv.find('div', class_='innerproductlist')

        productId = innerProductDiv.get('id')
        productCode= innerProductDiv.get('data-productcode')
        productName = innerProductDiv.get('data-productname')
        netPrice=innerProductDiv.get('data-productprice')
        anchor = innerProductDiv.find('a')
        availabilityUrl= anchor.get('href')
        grossPriceSpan= productDiv.find('span', class_='productlist-price')
        grossPrice=float(grossPriceSpan.find('span',class_='product-price-amount').text.strip().replace(',', '.')) if grossPriceSpan else None
        attributesDiv=productDiv.find('div',class_='productlist-usplist')
        attributesList = attributesDiv.find('ul') if attributesDiv else None
        attributes = [li.text.strip() for li in attributesList.find_all('li')] if attributesList else None
        composition = attributes[0] if attributes and len(attributes) > 0 else None
        needleStrength = attributes[1] if attributes and len(attributes) > 1 else None
        
        productInfo = {
            'productId': productId,
            'productCode': productCode,
            'productName': productName,
            'netPrice': float(netPrice),
            'availabilityUrl': availabilityUrl,
            'availability': None,
            'grossPrice': grossPrice,
            'composition': composition,
            'needleStrength': needleStrength
        }
        productList.append(productInfo)

    return productList

def readAvailabilityFromHtml(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    availableSpan = soup.find('span', class_='stock-green')
    unavailableSpan = soup.find('span', class_='stock-red')

    return availableSpan.text.strip() if availableSpan else unavailableSpan.text.strip() if unavailableSpan else None
