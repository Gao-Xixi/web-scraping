import requests
from bs4 import BeautifulSoup



class Product():
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
def func(soup):
    products = []
    product_names = soup.find_all('div', class_='pt-title')
    product_prices = soup.find_all('div', class_='pi-secondary-price')
    product_weights = soup.find_all('span', class_='pt-weight')
    print(product_names)
    for i in range(len(product_names)):
        p = Product(product_names[i].text, product_prices[i].span.text,product_weights[i].text)
        products.append(p)
        print(p.name, p.price, p.weight)



def main():
    print("Please enter the product name you wanna buy: ")
    keyword = input('>')
    re = requests.get(f"https://www.metro.ca/en/search?filter={keyword}&freeText=true")
    soup = BeautifulSoup(re.text, 'lxml')
    func(soup)

if __name__ == "__main__":
    main()
