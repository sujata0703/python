n=int(input('enter no'))
n1=2
while n1 <= n:
    isprime = True
    for i in range(2,n1):
        if n1%i == 0:
            isprime = False
            break
    if isprime == True:
       print(n1)
    n1 = n1 + 1






