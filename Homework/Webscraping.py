from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://learnwithjeff.azurewebsites.net/scrapedemo'

# opening connection, grabbing the page
r = uReq(url)
webpage = r.read()
r.close()

# HTMl parsing
webinfo = soup(webpage, "html.parser")

container = webinfo.find_all('td')

for row in container:
    print(row.text)
