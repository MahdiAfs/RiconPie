
import tldextract
 
# Get URL from user
url = input("Enter URL: ")
 
# Extract information from URL
a = tldextract.extract(url)
 
# Print all extracted information
print("The result after extraction is:", a)
 
# Print only the domain name
print(f'{a.domain}.{a.suffix}')
