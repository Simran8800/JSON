import json


python_obj=open("Text.txt","r")
a=json.load(python_obj)
print(type(a))
python_obj.close()
