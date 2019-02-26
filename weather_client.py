#https://openweathermap.org/appid
from urllib.request import urlopen
import bs4
import xmltodict
import json
import pprint

class Client_Web(object):
    """docstring fo Client_Web."""
    def __init__(self):
        pass

    def do_request(self):

        f = urlopen("http://api.openweathermap.org/data/2.5/find?q=Lleida&unit=metric&appid=69db18b86a5554a2d6aaa9b581417ce9&mode=json&lang=es")
        data = f.read()
        f.close()
        return data

    #def process_weather(self,html):
    #    tree = bs4.BeautifulSoup(html,features="lxml")
    #    temperature= tree.find("temperature")
    #    weather = tree.find("weather")
    #    return (temperature["value"]+" and "+ weather["value"])

    def process_weather(self,html):
        #dic = xmltodict.parse(html)
        #print(dic["cities"])
        dic = json.loads(html)
        #pprint.pprint(dic)
        temp = dic['list'][0]['main']['temp']
        wheather = dic['list'][0]['weather'][0]['description']
        return (str(temp)+" and "+wheather)




    def run(self):
        data = self.do_request()
        data = self.process_weather(data)
        print(data)


if __name__=="__main__":
    client= Client_Web()
    client.run()
