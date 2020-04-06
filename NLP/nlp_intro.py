#import urllib.request
#response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
#html = response.read()
#print(html)


#soup = BeautifulSoup(html,'html5lib')
#text = soup.get_text(strip = True)
#print(text)

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

reg_url = "https://www.investors.com/tag/apple-stock-news/"
reg_url = "https://seekingalpha.com/symbol/AAPL"
reg_url = "https://www.nltk.org/"
reg_url = "https://www.fool.com/quote/nasdaq/apple/aapl/" #WORKED -> important links are not http
reg_url = "https://www.fool.com/quote/nasdaq/tesla/tsla/"
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
req = Request(url=reg_url, headers=headers) 
html = urlopen(req).read() 

soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

