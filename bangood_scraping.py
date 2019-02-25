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
        products = tree.find_all("span","title")

        for product in products:
            self.process_product(product.find("a")["href"])


    def process_product(self,product):
        html = self.do_request(product)
        tree = bs4.BeautifulSoup(html, features="lxml")

        title = tree.find("div","title_hd")
        print("Name of product:",title.find("h2")["data-oldtext"])

        current_price = tree.find("div","item_now_price")
        print("Current price:",current_price.text)

        #old_price = tree.find("div","vipbox")
        #old_price=old_price.find("span","vip_old_price")
        #print(old_price)
        print("\n")

    def run(self):
        data = self.do_request()
        self.process_all_products(data)

if __name__=="__main__":
    client = Client_Web()
    client.run()
