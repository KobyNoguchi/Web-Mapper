from bs4 import BeautifulSoup as bs
import requests
url = 'http://bing.com'
r = reauests.get(url)

tree = bs(r.text, 'html.parser') # parse into tree
for link in tree. find _all('a'): # Find all "a" anchor elements
    print(f"{link.get('href')} -> {link.text}")

    

