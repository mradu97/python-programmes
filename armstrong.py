n= int(input("enter any no"))
sum=0
i=n
while(i>0):
    r=i%10
    i=i/10
    
    sum=sum+(r*r*r)
    
if(sum==n):
    print("the no" ,n,"is an armstrong no")
else:
    print("the no ",n,"is not an armstrong no")
