import requests
from bs4 import BeautifulSoup

url = requests.get('https://melcom.com/categories/mobiles-computers.html')

soup = BeautifulSoup(url, 'html.parser')
print(soup)
