#Two types of module in python
# - Built in Modules
# - External Modules
import math
import os
import My_Module
import requests

print(math.sqrt(16))
My_Module.hello()
r = requests.get("https://www.google.com")
print(r.text)