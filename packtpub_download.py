#https://www.packtpub.com//packt/offers//free-learning
#https://bigdata-madesimple.com/scrape-data-web-using-python/

from urllib.request import urlopen
import bs4

class Client_Web(object):
    """docstring fo Client_Web."""
    def __init__(self):
        pass

    def download_html_page(self):
        file = urlopen("https://www.packtpub.com//packt/offers//free-learning")
        html= file.read()
        file.close()
        return html

    def search_relevant_information(self,html_file):
        tree = bs4.BeautifulSoup(html_file,features="lxml")
        information=tree.find_all("div","respoPage") #Imposible conseguir datos
        print(information)



    def run(self):
        html = self.download_html_page()
        self.search_relevant_information(html)


if __name__=="__main__":
    client= Client_Web()
    client.run()
