import os
fname=input("enter filename")
if os.path.isfile(fname):
    print("file exists:" ,fname)
    f=open(fname,'r')
    lcount=0
    for line in f:
        lcount=lcount+1
    print("the no of lines",lcount)