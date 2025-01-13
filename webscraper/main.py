from bs4 import BeautifulSoup
import requests

url = 'https://www.pricecharting.com/console/pokemon-scarlet-&-violet-151?sort=model-number&model-number=&exclude-variants=true&show-images=false&in-collection='
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

# Find all table rows with product information
product_rows = soup.find_all('tr', {'id': lambda x: x and x.startswith('product-')})

for row in product_rows:
    # Extract product name
    product_name = row.find('td', {'class': 'title'}).get_text(strip=True)
    
    # Extract prices
    used_price = row.find('td', {'class': 'price numeric used_price'}).find('span', {'class': 'js-price'}).get_text(strip=True)
    cib_price = row.find('td', {'class': 'price numeric cib_price'}).find('span', {'class': 'js-price'}).get_text(strip=True)
    new_price = row.find('td', {'class': 'price numeric new_price'}).find('span', {'class': 'js-price'}).get_text(strip=True)
    
    # Print the extracted data
    print(f"Product: {product_name}")
    print(f"Used Price: {used_price}")
    print(f"CIB Price: {cib_price}")
    print(f"New Price: {new_price}")
    print("-" * 40)
