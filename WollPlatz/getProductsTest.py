
from getProducts import getProducts
import csv
import sys
import os

def main():
    query = os.getenv("QUERY")
    if not query:
        print("Please set the QUERY environment variable.")
        sys.exit(1)
   
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