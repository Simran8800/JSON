
import json


python_obj=open("text.json","r")
a=json.load(python_obj)
print(type(a))
python_obj.close()

