import requests

#from requests import *

response = requests.get('http://google.com')

print(response.text)