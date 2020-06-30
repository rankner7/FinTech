import urllib.request
from bs4 import BeautifulSoup
from nltk import tokenize

response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
#print(text)

tokens = [t for t in text.split()]

new_tokens = tokenize.tokenize(text)
print(new_tokens)
