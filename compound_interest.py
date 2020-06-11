def compoundi(p,r,t):
    ci=p*(pow((1+r/100),time))
    return(ci)


x = int(input("enter principle amount"))
y = int(input("enter rate"))
z = int(input("enter time period"))
k = compoundi(x,y,z)
print(k)
