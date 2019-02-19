from urllib.request import urlopen
import bs4

class Client_Web(object):
    """docstring fo Client_Web."""
    def __init__(self):
        pass

    def do_request(self):

        f = urlopen("http://api.openweathermap.org/data/2.5/find?q=Lleida&unit=metric&appid=69db18b86a5554a2d6aaa9b581417ce9&mode=xml")
        data = f.read()
        f.close()
        return data

    def process_weather(self,html):
        tree = bs4.BeautifulSoup(html,features="lxml")
        temperature= tree.find("temperature")
        weather = tree.find("weather")
        print (temperature["value"]+" and "+ weather["value"])
        return None

    def run(self):
        data = self.do_request()
        data = self.process_weather(data)
        #print(data)


if __name__=="__main__":
    client= Client_Web()
    client.run()
