import requests
from bs4 import BeautifulSoup
import json



def scrape_product(url , selector):
    html = requests.get(url)
    html.raise_for_status()
    soup = BeautifulSoup(html.content , 'html.parser')
    product_price = soup.select_one(f"{selector}")
    if product_price:
        product_price = product_price.get_text().strip().replace("$", "")
    return product_price



def data_read(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def write_data(filename , data):
    with open(filename , 'w' , encoding='utf-8') as f:
        json.dump(data , f , indent=4)

def product_list_function(filename):
    data = data_read(filename)
    product_list = []
    for product in data.keys():
        product_list.append((product , data[product]["selector"]))
    return product_list


