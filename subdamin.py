
import dns.resolver
import tldextract

def sub(url):

    extracted_infoinfo = tldextract.extract(url)
    domain = f'{extracted_infoinfo.domain}.{extracted_infoinfo.suffix}'

    file = open("wordlist.txt")
    content = file.read()
    subdomains = content.splitlines()

    ali = []
    domains = ['']
    if domain is not domains:

        subdomain_store = []
        for subdoms in subdomains:
            try:
                

                ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', "A")
                
                subdomain_store.append(ip_value)

                domains = [domain]

                for ip in ip_value:

                    ali.append(f'{subdoms}.{domain} : {ip}')

                else:
                    pass
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except KeyboardInterrupt:
                pass

    return ali

print(sub('https://google.com'))

