from getProducts import getProducts
import sys
import os

def main():
    query = os.getenv("QUERY")
    if not query:
        print("Please set the QUERY environment variable.")
        sys.exit(1)

    products=getProducts(query)
    print(f"({products})")

if __name__ == "__main__":
    main()