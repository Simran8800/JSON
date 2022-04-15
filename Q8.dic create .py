import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=  ["anuradha","HR","25","40000"]
d= ["Abhishek","manager","29","63000"]
keys=['name','designation','age','salary']
k={}
m={}
n={}
d={}
var=({'k':k,"m":m,"n":n,"d":d})
for i in range(len(a)):
    k.update({keys[i]:a[i]})
for j in range(len(b)):
    m.update({keys[j]:b[j]})
for p in range(len(c)):
    n.update({keys[p]:c[p]})
for f in range(len(d)):
    d.update({keys[f]:d[f]})
with open("simran q no8",'w')as g:
    json.dump(var,g,indent=5)