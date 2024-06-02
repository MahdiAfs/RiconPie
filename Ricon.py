import dns.resolver
import requests
from bs4 import BeautifulSoup
import re
import socket
import tldextract
import argparse

site_map = {}
url =""

def argges():
    
    parser = argparse.ArgumentParser(description='Process some inputs.')

    parser.add_argument('--input', type=str, help='input to run the program')
    parser.add_argument('--information', help=' information for program' , required=False)
    parser.add_argument('--Hwork', help='information for program work' , required=False)


    args = parser.parse_args()

    if args.input is not None:
        url = args.input
        return url
    if args.information:
        print(f"This project is to identify the target for cyber attack.")
    if args.Hwork:
        print(f" When the user enters the input, it will display all the links of the site \n and all the subdomains of the links and the IPs of the links and all the open ports of the IPs \n and title lines in addition to the Status codes of the links.")


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


def depth():
    j = 0
    url = site_Link(argges())
    site_map[argges()] = url
    for i in range(1):
        while j < len(url):
            link = url[j]
            site_map[link] = site_Link(url[j])
            j = j + 1


def status(input):

    response = ''
    try:
        response = requests.get(input)
   
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
            return("Unknown status code",":", response.status_code)
    except:
        pass 


def title(title_input):

    try:
        response = requests.get(title_input)

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title 
    except:
        pass

_domains = ['']
def sub(_link):

    extracted_infoinfo = tldextract.extract(_link)
    domain = f'{extracted_infoinfo.domain}.{extracted_infoinfo.suffix}'

    file = open("wordlist.txt")
    content = file.read()
    subdomains = content.splitlines()

    
    if domain not in _domains:

        subdomain_store = []
        all_subdomain = []

        for subdoms in subdomains:
            try:
 
                ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', "A")
                subdomain_store.append(ip_value)
                _domains.append(domain)

                for ip in ip_value:
                    all_subdomain.append (f'{subdoms}.{domain} : {ip}')

            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except KeyboardInterrupt:
                pass
    else:
            all_subdomain = [None]
    return all_subdomain





def ip(ip_input):

    extracted_info = tldextract.extract(ip_input)
    if extracted_info.subdomain is not None:
        ip_input = f'{extracted_info.domain}.{extracted_info.suffix}'
    else:    
        ip_input = f'{extracted_info.subdomain}.{extracted_info.domain}.{extracted_info.suffix}' 

    ip_output = (socket.gethostbyname(ip_input))
        
    return ip_output



def port_scan(ip_input):

    ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]
    port_output=[]
    for port in ports:  

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        result = sock.connect_ex((ip_input, port))
        if result == 0:
            port_output.append(port)
        else:
            pass
        sock.close()

    return port_output


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

  

depth()

file = open("report.txt", 'a')
for key,links in site_map.items():
    # file.writelines(f'\nsubdomain     {key}: \n {sub(key)}')
    file.writelines(f'\nip and open port     {key} : \n {ip(key)} : {port_scan(ip(key))}')
    file.writelines(f'\nstatuscod    {key} :{status(key)} \n {title(key)}')
    file.writelines(f'\ntitle    {key} : {title(key)}')
    file.writelines(f'\nregEx    {key} : {regex(key)}')
    # print(key)
    for link in links:
        # file.writelines(f' \t \nsubdomain {key}: \n {sub(key)}')
        file.writelines(f' \t \nip and open port   {key} : \n {ip(key)} : {port_scan(ip(key))}')
        file.writelines(f' \t \nstatuscod   {key} :{status(key)} \n {title(key)}')
        file.writelines(f' \t \ntitle   {key} : {title(key)}')
        file.writelines(f' \t \nregEx   {key} : {regex(key)}')
file.close()        
