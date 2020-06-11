def si(p,r,t):
    si = (p*r*t)/100
    return si

i = int(input("principle amount"))
j = int(input("rate"))
k = int(input("time period"))
l = si(i,j,k)
print(l)
