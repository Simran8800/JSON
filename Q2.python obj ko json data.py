import requests
import json


a={"name": "David", "class": "I", "age": 6}

with open("information.json",'w')as f:
    json.dump(a,f,indent=4)
