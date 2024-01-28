
from getProducts import getProducts
import csv
import sys
import os

def main():
    query = os.getenv("QUERY")
    if not query:
        print("Please set the QUERY environment variable.")
        sys.exit(1)
    ## Mockdata to test the csv writer because Wollplatz.de is blocked by cloudflare
        """[
            {
                'productId': 'pid-38559',
                'productCode': 'bwdmc0111008F',
                'productName': 'DMC 1008F Mouliné Satin Stickgarn 8m',
                'netPrice': 1.03,
                'availabilityUrl': 'https://www.wollplatz.de/wolle/dmc/dmc-1008f-mouline-satin-stickgarn-8m',
                'availability': Verfügbar,
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
                'availability': Verfügbar,
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
                'availability': Verfügbar,
                'grossPrice': 3.59,
                'composition': '100% Polyester',
                'needleStrength': 'Thread'
            }
        ]
        """
    products=getProducts(query)
    filename=f"{query}.csv"
    writeCsv(products, filename)
    print(f"({products})")

    
def writeCsv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'productId',
            'productCode',
            'productName',
            'netPrice',
            'availabilityUrl',
            'availability',
            'grossPrice',
            'composition',
            'needleStrength'
        ]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == "__main__":
    main()