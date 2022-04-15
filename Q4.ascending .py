dic={'4': 5, '6': 7, '1': 3, '2': 4}
# for k, v in sorted(a.items()):
#         print((k, v))


for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print(dic)
        
    
