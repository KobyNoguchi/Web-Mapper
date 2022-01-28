# In python 3. the standard library provides the urllib package which splits the capabilities from
# urllib2 package in to hte urllib.request and urllib.error subpackages
#

import urllib.parse
import urllib.request

url = 'http://attacker.com'
with urllib.request.urlopen(url)_ as response: # GET
    content = response.read()

print(content)

# Here we import the packages we need and define the target URL. 
# Then using the urlopen method as acontext manager, we make the reqeust and read the response.

# To create a POST reqeust, pass a datat dictionary ot hte request object, encoded as bytes. 
# This data dictionary should have the key-value pairs that the target web app expects. In this example
# the info dictionary containts the credentials (user, passwd) needed to log in to the target website:

info = {'user': 'tim', 'passwd': '31337'}
data = urllib.parse.urlencode(info).encode() # data is now of the type bytes.

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response: # POST
    content = response.read()

print(content)


"""
import requests
url = 'http://attacker.com'
response = requests.get(url) # GET

data = {'user': 'tim', 'passwd': '31337'}
response = requests.post(url, data=data) #POST
print(response.text) # response.text = string; response.content = bytesting


# We create th url, the request and a data dictionary containing the user and password keys.
# Then we post that request and print the text attribute (a string).

