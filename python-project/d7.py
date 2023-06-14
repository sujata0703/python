word=input("eneter any string")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
for i,j in d.items():
    print(i,j)


