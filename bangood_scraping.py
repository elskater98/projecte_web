from urllib.request import urlopen
import bs4

class Client_Web(object):
    def __init__(self):
        pass

    def do_request(self,str="https://www.banggood.com/es/Flashdeals.html"):
        file = urlopen(str)
        data = file.read()
        file.close()
        return data

    def process_all_products(self,html):
        tree = bs4.BeautifulSoup(html,features="lxml")
        self.print_product_information(self.get_titles(tree),self.get_prices(tree))


    def get_titles(self,tree):
        list_product = []
        products = tree.find_all("span", "title")

        for product in products:
            list_product.append(product.find("a").text)

        return list_product

    def get_prices(self,tree):
        list_prices = []
        price_items = tree.find_all("div", "priceitem")

        for price in price_items:
            list_prices.append((price.find("span","price").text,price.find("span","price_old").text))

        return list_prices

    def print_product_information(self, list_product, list_prices):

        for i in range(len(list_prices)):
            print("TITLE: ", list_product[i],
                  "\nCURRENT PRICE: ", list_prices[i][0],
                  "\nOLD PRICE: ",list_prices[i][1])
            print("\n")


    def run(self):
        data = self.do_request()
        self.process_all_products(data)

if __name__=="__main__":
    client = Client_Web()
    client.run()
