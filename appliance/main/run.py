from bs4 import BeautifulSoup as bs
import requests




url = "https://frankotrading.com/?s=samsung&post_type=product"
page = requests.get(url)

soup = bs(page.content, 'html.parser')
lists = soup.find_all('div', class_="product_cat-samsung-mobile-phones")

for list in lists:
    image = list.find('img', class_="attachment-woocommerce_thumbnail")
    title = list.find('h3', class_="product-title")
    price = list.find('bdi')
    product = [image, title, price]
    print(product)