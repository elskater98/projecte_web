from urllib.request import urlopen
import bs4

class Client_Web(object):
    """docstring fo Client_Web."""
    def __init__(self):
        pass

    def do_request(self,str="https://www.banggood.com/es/Flashdeals.html"):
        file = urlopen(str)
        data = file.read()
        file.close()
        return data

    def process_all_products(self,html):
        tree = bs4.BeautifulSoup(html,features="lxml")
        titles = tree.find_all("span","title")
        references=[]

        for x in titles:
            references.append(x.find("a")["href"])

        return references

    def process_product(self,list_products):
        data = self.do_request(list_products)
        tree = bs4.BeautifulSoup(data, features="lxml")

        title = tree.find("div","title_hd")
        print("Name of product:",title.find("h2")["data-oldtext"])

        current_price = tree.find("div","item_now_price")
        print("Current price:",current_price.text)

       # old_price = tree.find("div","item_old_price")
        #print(old_price.text)


    def run(self):
        data = self.do_request()
        list_product=self.process_all_products(data)
        max_len=len(list_product)

        for x in range(max_len):
            self.process_product(list_product[x])




if __name__=="__main__":
    client = Client_Web()
    client.run()
