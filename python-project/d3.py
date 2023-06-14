n= int(input("enter how many students"))
d={}
for i in range(n):
    name=input('enter student name')
    marks=int(input('enter marks'))
    d[name]=marks
print(d)
print('#'*20)
print('Name','\t\t','Marks')
print('#'*20)
for key in d:
    print(key,'\t\t',d[key])
