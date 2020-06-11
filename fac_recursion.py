def factorial(n,i):
    n = n * i    
    if i >1:
        factorial(n,i-1)
    return(n)

n = int(input("enter a no"))
i=n-1
f=factorial(n,i)
print(f)
