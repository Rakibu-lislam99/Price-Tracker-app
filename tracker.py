import requests
from bs4 import BeautifulSoup
import json, datetime , alarts,time


def data_read(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def write_data(filename , data):
    with open(filename , 'w' , encoding='utf-8') as f:
        json.dump(data , f , indent=4)





def track_product(url , selector):
    html = requests.get(url)
    html.raise_for_status()
    soup = BeautifulSoup(html.content , 'html.parser')
    product_price = soup.select_one(f"{selector}")
    if product_price:
        product_price = product_price.get_text().strip().replace("$", "")
    return product_price


def main():
    json_data = data_read('data.json')
    for url in json_data.keys():
        current_price = float(track_product(url , json_data[url]['selector']))
        if not current_price:
            continue
        previous_price = json_data[url]['price']
        if current_price - previous_price > 100:
            message = "Price increased $100"
            alarts.send_email_message("Price increased $100")
            alarts.send_telegram_message("Price increased $100")
        elif previous_price - current_price > 100:
            message = "Price decreased $100"
            alarts.send_email_message("Price decreased $100")
            alarts.send_telegram_message("Price decreased $100")
        elif current_price > previous_price:
            message = "Price increased"
        elif previous_price > current_price:
            message = 'Price decreased'
        else:
            message = 'Price decreased'
        json_data[url]['price'] = current_price
        json_data[url]['last time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


    write_data('data.json' , json_data)


while True:
    main()

    time.sleep(120)