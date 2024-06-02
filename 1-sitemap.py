import requests
from bs4 import BeautifulSoup
from threading import Thread
site_map = {}
url =""



def site_Link(url):
    
    links = []
    try:
        respaon = requests.get(url)
        html = BeautifulSoup(respaon.content , "html.parser")
    
        
        for link in html.find_all("a"):

            href = link.get("href")

            if href is not None  and  href.startswith("http"):

                links.append(href)
    except:
        pass
    
    return links


url = site_Link("https://mrbug.ir")
site_map["https://wikipedia.org"] = url


def depth():

    j = 0
    
    for i in range(1):

        while j < len(url):

            link = url[j]
            site_map[link] = site_Link(url[j])
            j = j + 1

depth()


trd = 50

for i in range(trd):

    t = Thread(target=site_Link)
    t.start
   



for key, links in site_map.items():
    print(key)
    for link in links:
        print("\t", link)
        



        
