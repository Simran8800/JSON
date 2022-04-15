import json
a={"s":12,"d":23}
with open("myfile.json","w")as f:
    json.dump(a,f,indent=4)
with open("myfile.json","r")as p:
    data=json.load(p)
    print(data)
print(json.dumps(a))
m=json.dumps(a)
print(json.loads(m))