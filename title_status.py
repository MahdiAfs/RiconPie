from bs4 import BeautifulSoup
import requests


url1 = 'https://www.wikipedia.org'
def title():

    response = requests.get(url1)

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string

    return title 


def status():
    
    response = requests.get(url1)
    if response.status_code == 200:
        return("Success",":", response.status_code)
    elif response.status_code == 301:
        return("Moved Permanently",":", response.status_code)
    elif response.status_code == 302:
        return("Found",":", response.status_code)
    elif response.status_code == 400:
        return("Bad Request",":", response.status_code)
    elif response.status_code == 401:
        return("Unauthorized",":", response.status_code)
    elif response.status_code == 403:
        return("Forbidden",":", response.status_code)
    elif response.status_code == 404:
        return("Page not found",":", response.status_code)
    elif response.status_code == 500:
        return("Internal server error",":", response.status_code)
    else:
        print("Unknown status code",":", response.status_code)


status()
title()