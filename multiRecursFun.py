def mul(a,b):
    print(a, " * ", b , " = ", a * b)
    if b < 11 :
        mul(a, b +1)

n = int(input("Enter any no"))
mul(n,1)
