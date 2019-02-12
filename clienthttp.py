from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """ClientWeb per la web eps."""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass
    def descargar_html(self):
        f = urlopen("http://www.eps.udl.cat/ca/")
        html= f.read()
        f.close()
        return html
    def buscar_activitats(self,html):
        arbre=bs4.BeautifulSoup(html,features="lxml")
        activitats=arbre.find_all("div","featured-links-item")
        return activitats

    def run(self):
        #Descargarme html
        html = self.descargar_html()
        #buscar activitats
        activitats=buscar_activitats(html)
        #imprimir resultat
        pass




if __name__=="__main__":
    c = ClientWeb()
    c.run()
