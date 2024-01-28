from scraper.index import readAvailabilityFromHtml, readProductsFromHtml
import unittest
import os



class TestGetProductNames(unittest.TestCase):
    def test_get_product_names(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(currentDir,"html", 'getProductsResponse.html')
        with open(file_path, 'r', encoding='utf-8') as file:
            getProductsResponse = file.read()

        result = readProductsFromHtml(getProductsResponse)
        expectedResult = [
            {
                'productId': 'pid-49320',
                'productCode': 'bwst330',
                'productName': 'Stylecraft Baby Sparkle',
                'netPrice': 3.72,
                'availabilityUrl': 'https://www.wollplatz.de/artikel/49320/stylecraft-baby-sparkle.html',
                'availability': None,
                'grossPrice': 4.43,
                'composition': None,  
                'needleStrength': None
            },
            {
                'productId': 'pid-18011',
                'productCode': 'bwst284',
                'productName': 'Stylecraft Bellissima DK',
                'netPrice': 3.51,
                'availabilityUrl': 'https://www.wollplatz.de/wolle/stylecraft/stylecraft-bellissima-dk',
                'availability': None,
                'grossPrice': 4.18,
                'composition': None,
                'needleStrength': None
            },
            {
                'productId': 'pid-48411',
                'productCode': 'bwst324',
                'productName': 'Stylecraft Fusion',
                'netPrice': 3.72,
                'availabilityUrl': 'https://www.wollplatz.de/artikel/48411/stylecraft-fusion.html',
                'availability': None,
                'grossPrice': 4.43,
                'composition': None,
                'needleStrength': None
            },
           ]
        self.assertEqual(result, expectedResult)

    def test_get_product_names(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(currentDir,"html", 'getProductsResponse2.html')
        with open(file_path, 'r', encoding='utf-8') as file:
            getProductsResponse = file.read()

        result = readProductsFromHtml(getProductsResponse)
        expectedResult = [
            {
                'productId': 'pid-38559',
                'productCode': 'bwdmc0111008F',
                'productName': 'DMC 1008F Mouliné Satin Stickgarn 8m',
                'netPrice': 1.03,
                'availabilityUrl': 'https://www.wollplatz.de/wolle/dmc/dmc-1008f-mouline-satin-stickgarn-8m',
                'availability': None,
                'grossPrice': 1.23,
                'composition': '100% Viskose',
                'needleStrength': 'Thread'
            },
            {
                'productId': 'pid-37568',
                'productCode': 'bwdmc011117MC',
                'productName': 'DMC 117MC Mouliné Special Stickgarn 8m',
                'netPrice': 1.61,
                'availabilityUrl': 'https://www.wollplatz.de/wolle/dmc/dmc-117mc-mouline-special-stickgarn-8m',
                'availability': None,
                'grossPrice': 1.92,
                'composition': '100% Mercerisiert Baumwolle',
                'needleStrength': 'Thread'
            },
            {
                'productId': 'pid-38526',
                'productCode': 'bwdmc011317W',
                'productName': 'DMC 317W Mouliné Metallise Stickgarn 8m',
                'netPrice': 3.02,
                'availabilityUrl': 'https://www.wollplatz.de/wolle/dmc/dmc-317w-mouline-metallise-stickgarn-8m',
                'availability': None,
                'grossPrice': 3.59,
                'composition': '100% Polyester',
                'needleStrength': 'Thread'
            }
        ]

        self.assertEqual(result, expectedResult)
        

class TestReadAvailabilityFromHtml(unittest.TestCase):
    def test_available_span(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(currentDir,"html", 'getProductAvailabilityResponseGreen.html')
        with open(file_path, 'r', encoding='utf-8') as file:
            availableResponse = file.read()
        result = readAvailabilityFromHtml(availableResponse)
        self.assertEqual(result, "Lieferbar")

    def test_unavailable_span(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(currentDir, "html",'getProductAvailabilityResponseRed.html')
        with open(file_path, 'r', encoding='utf-8') as file:
            unavailableResponse = file.read()
        result = readAvailabilityFromHtml(unavailableResponse)
        self.assertEqual(result, "Nicht mehr verfügbar.")

    def test_both_spans_missing(self):
        html_content = """
        <div>No spans here</div>
        """
        result = readAvailabilityFromHtml(html_content)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
