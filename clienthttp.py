from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """ClientWeb per la web eps."""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def descargar_html(self):
        f = urlopen("http://www.eps.udl.cat/ca/")
        html = f.read()
        f.close()
        return html

    def buscar_activitats(self,html):
        arbre=bs4.BeautifulSoup(html,features="lxml")
        activitats=arbre.find_all("div","featured-links-item")
        activity_list = []
        for activity in activitats:
            title = activity.find("span","flink-title")
            print(title.text)
            link = activity.find("a")
            activity_list.append((title.text,link["href"]))
            print(link.text)
        return activitats_list

    def run(self):
        #Descargarme html
        html = self.descargar_html()
        #buscar activitats
        activitats = self.buscar_activitats(html)
        #imprimir resultat





if __name__=="__main__":
    c = ClientWeb()
    c.run()
