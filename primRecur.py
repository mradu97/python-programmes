pr  = 0
i =2
def prime_rec(n):
    global pr
    global i

    if (n % i) == 0:
          pr=1

    
    i = i +1
    
    if n > i:
        prime_rec(n)
        
    if pr==0:
        print("no is prime")
    else:
        print("no is not prime")

j = int(input("Enter some number"))
prime_rec(j)
