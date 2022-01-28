import urllib2
url = 'https://www.nostarch.com'
response = urllib2.urlopen(url) # GET
print(response.read())
response.close()

# The simplest example of how to make a get request to a website
# We pass in a URL to the urlopen function, which returns a file like object
# that allows us to read back the body of what the remote web server returns.
# 
# Since we're just fetching the raw page from the NO Starch website, no JavaScript or other Client side languages will execute.



"""
import urllib2
url = "https://www.nostarch.com"
headers = {'User-Agent': "Googlebot"}

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print(response.read())
response.close()

"""

# Above example shows how to creat the same GET request by using the Request class in urllib2 
# as well as defining a custom User-Agent Http header

