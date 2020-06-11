def prime(n):
    pr=0
    for i in range (2,n,1):
        if n % i == 0:
            pr=1
    if pr==0:
        print("no is prime")
    else:
        print("no is not prime")

a = int(input("enter any no"))
prime(a)
    
