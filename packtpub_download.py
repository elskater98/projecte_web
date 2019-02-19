#https://www.packtpub.com//packt/offers//free-learning
#https://bigdata-madesimple.com/scrape-data-web-using-python/

from urllib.request import urlopen
import bs4

class Client_Web(object):
    """docstring fo Client_Web."""
    def __init__(self):
        super(Client_Web, self).__init__()

    def download_html_page(self):
        html_file = urlopen("https://www.packtpub.com//packt/offers//free-learning")
        print(html_file)
        html_file.close()


if __name__=="__main__":
    client= Client_Web()
    client.download_html_page()
