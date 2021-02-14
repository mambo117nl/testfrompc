import sys
from os import rename
import requests
import math



print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello,{}'.format(who_to_greet)
    return greeting

  

r = requests.get('http://google.com')
print(r.status_code)
print("put len gihub")
