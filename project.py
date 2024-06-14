from random import randint
import time
import requests
from bs4 import BeautifulSoup
import csv


# # to test is or not everything OK

# url_for_testing = 'https://pcroom.ge/mausebi?page=1'
# resp = requests.get(url_for_testing)
# print(resp)
# print(resp.status_code)
# print(resp.headers)
# print(resp.headers['Content-Type'])
# print(resp.text)


file = open('mouse.csv', 'w', encoding='utf-8_sig', newline='\n')
write_object = csv.writer(file)
write_object.writerow(['Name', 'Type', 'Price', 'Currancy'])

ind = 1
while ind < 6:
    url = f'https://pcroom.ge/mausebi?page={ind}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    mouse_section = soup.find('div', class_='row cat_prod')
    all_mouse = mouse_section.find_all('div', class_="product-block-inner")
    for mouse in all_mouse:
        mouse_info = mouse.h4.a.text.strip()
        mouse_prices = mouse.find('div', class_='product-details').p
        mouse_type = mouse_info[:(mouse_info.find('-') - 1)]
        mouse_name = mouse_info[(mouse_info.find('- ') + 2):]
        price_info = mouse_prices.text.strip()
        index = (mouse_prices.text.strip().find('ლ'))
        price = price_info[ : index].strip()
        currancy = price_info[index : (index + 1)]
        write_object.writerow([mouse_name, mouse_type, price, currancy])
    ind += 1
    time.sleep(randint(2, 10))
    
