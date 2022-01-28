# Suppose we have the HTML content from a request stored in a variable named content.
# Using lxml, you could retrieve the content and parse the links as follows:

from io import BytesIO
from lxml import etree

#we import the BytesIO class from the io module becasue we'll need it in 
# order to use a byte string as a file object when we parse the HTTP response.

import requests

url = 'https://nostartch.com'
r = requests.get(url) #GET
content = r.content   # content is of type 'bytes'

# We perform the GET request as usual and then use the lxml HTML parser to parse the response.
# The parser expects a file-like object or a filename. 

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser) # Parse into tree

# The BytesIO class enables us to use the returned byte string content as a file-like object ot pass the lxml parser.

for link in content.findall('//a'): # find all "a" anchor elements.
    print(f"{link.get('href')} -> {link.text}")

# the f string allows us to include hte result of a function call (link.get('href')) or a plain value (link.text) in our string.


