def factorial(n):
    f=n
    i=n
    while i>1:
        i=i-1
        f=f*i
        
    return f


n = int(input("enter any no to calculate its factorial"))
k = factorial(n)
print("Factorial is ",k)
