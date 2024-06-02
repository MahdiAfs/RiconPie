import requests
import re
from bs4 import BeautifulSoup

def regex(input):
        
    try:
        respaon = requests.get(input)

        html = BeautifulSoup(respaon .content , "html.parser")

        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        email = re.findall(pattern , str(html))

        patterna = r"/^0\d{2,3}-\d{8}$/gm"

        phone = re.findall(patterna , str(html))


        return email , phone
    
    except:
        pass