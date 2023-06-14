n = int(input("input no"))
if n <= 1:
    print(" its not aprime no")
else:
    isprime = True
    for i in range(2,n):
        if n%i == 0:
            isprime = False
            break
    if isprime == True:
        print("yoy entered prime no")
    else:
        print("you entered not a prime")



